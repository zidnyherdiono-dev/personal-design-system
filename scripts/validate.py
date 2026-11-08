#!/usr/bin/env python3
"""Repository validator: structure, docs, catalog sync, links, tokens.

Run: python scripts/validate.py   (exit code 0 = all checks pass)
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, warnings, passed = [], [], []

REQUIRED_FILES = [
    "README.md", "AGENTS.md", "LICENSE", ".gitignore",
    "tokens/README.md", "tokens/STATUS.md", "tokens/tokens.json", "tokens/tokens.css",
    "foundations/README.md", "foundations/color.md", "foundations/typography.md",
    "foundations/spacing.md", "foundations/motion.md", "foundations/elevation.md",
    "foundations/accessibility.md",
    "components/README.md",
    "patterns/README.md",
    "templates/README.md", "templates/catalog.json",
    "previews/README.md", "previews/preview.css", "previews/preview.js",
    "index.html",
    "docs/workflow.md", "docs/contributing.md", "docs/documentation-standard.md",
    "docs/ai-integration.md",
    "scripts/serve.py", "scripts/validate.py",
]

def ok(msg): passed.append(msg)
def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)

# 1. Required files
for rel in REQUIRED_FILES:
    (ok if os.path.isfile(os.path.join(ROOT, rel)) else err)(f"file exists: {rel}")

# 2. Per-folder README for content dirs
for folder in ["tokens", "foundations", "components", "patterns", "templates", "previews", "docs", "scripts"]:
    p = os.path.join(ROOT, folder, "README.md")
    if os.path.isfile(p):
        ok(f"README present: {folder}/")
    else:
        (err if folder != "scripts" else warn)(f"README missing: {folder}/")

# 3. Component/pattern completeness: html+css+README per folder
for base in ["components", "patterns"]:
    base_dir = os.path.join(ROOT, base)
    for name in sorted(os.listdir(base_dir)):
        folder = os.path.join(base_dir, name)
        if not os.path.isdir(folder):
            continue
        for ext in [".html", ".css", "README.md"]:
            f = name + ext if ext != "README.md" else "README.md"
            if os.path.isfile(os.path.join(folder, f)):
                ok(f"{base}/{name}/{f}")
            else:
                err(f"missing {base}/{name}/{f}")

# 4. Component README 4-section standard
REQUIRED_SECTIONS = ["## Variants", "## States", "## Responsive", "## Accessibility"]
for base in ["components", "patterns"]:
    base_dir = os.path.join(ROOT, base)
    for name in sorted(os.listdir(base_dir)):
        readme = os.path.join(base_dir, name, "README.md")
        if not os.path.isfile(readme):
            continue
        text = open(readme, encoding="utf-8").read()
        for sec in REQUIRED_SECTIONS:
            if sec.lower() in text.lower():
                ok(f"{base}/{name}/README has '{sec}'")
            else:
                (err if base == "components" else warn)(f"{base}/{name}/README missing '{sec}'")

# 5. tokens.json validity + provisional guard
tj = os.path.join(ROOT, "tokens", "tokens.json")
try:
    data = json.load(open(tj, encoding="utf-8"))
    if data.get("_meta", {}).get("status") == "PROVISIONAL":
        ok("tokens.json valid JSON + status PROVISIONAL")
    else:
        warn("tokens.json _meta.status is not PROVISIONAL (check tokens/STATUS.md)")
    for group in ["color", "typography", "spacing", "radius", "shadow", "motion"]:
        (ok if group in data else err)(f"tokens.json has group: {group}")
except Exception as e:
    err(f"tokens.json invalid: {e}")

# 6. catalog.json validity + entry paths exist
cj = os.path.join(ROOT, "templates", "catalog.json")
try:
    cat = json.load(open(cj, encoding="utf-8"))
    ok("catalog.json valid JSON")
    for t in cat.get("templates", []):
        p = os.path.join(ROOT, t["path"].rstrip("/"))
        entry = os.path.join(ROOT, t["entry"])
        (ok if os.path.isdir(p) else err)(f"catalog path exists: {t['path']}")
        (ok if os.path.isfile(entry) else err)(f"catalog entry exists: {t['entry']}")
        if t.get("designFinal") is True:
            warn(f"template {t['id']} marked designFinal=true — ensure design direction was decided")
except Exception as e:
    err(f"catalog.json invalid: {e}")

# 7. Markdown links resolve (relative links only)
LINK_RE = re.compile(r"\[[^\]]*\]\((?!https?://|#|mailto:)([^)]+)\)")
md_checked = 0
for dirpath, _dirs, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in files:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(dirpath, fn)
        text = open(path, encoding="utf-8").read()
        for target in LINK_RE.findall(text):
            target = target.split("#")[0].strip()
            if not target or "<" in target:
                continue  # template placeholder (e.g. <name>.html), not a real link
            md_checked += 1
            resolved = os.path.normpath(os.path.join(dirpath, target))
            if os.path.exists(resolved):
                ok(f"link ok: {os.path.relpath(path, ROOT)} -> {target}")
            else:
                err(f"broken link: {os.path.relpath(path, ROOT)} -> {target}")
ok(f"checked {md_checked} relative markdown links")

# 8. HTML sanity: each .html parses and has <title> + viewport
class Chk(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = set()
    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)

for dirpath, _dirs, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in files:
        if not fn.endswith(".html"):
            continue
        path = os.path.join(dirpath, fn)
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, ROOT)
        try:
            c = Chk()
            c.feed(text)
            ok(f"html parses: {rel}")
            if "title" in c.tags: ok(f"has <title>: {rel}")
            else: warn(f"no <title>: {rel}")
            if 'name="viewport"' in text: ok(f"has viewport meta: {rel}")
            else: warn(f"no viewport meta: {rel}")
        except Exception as e:
            err(f"html parse failed: {rel}: {e}")

# 9. JS syntax smoke (node if available, else skipped)
import shutil, subprocess
if shutil.which("node"):
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for fn in files:
            if fn.endswith(".js"):
                path = os.path.join(dirpath, fn)
                r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
                rel = os.path.relpath(path, ROOT)
                if r.returncode == 0:
                    ok(f"js syntax ok: {rel}")
                else:
                    err(f"js syntax error: {rel}: {r.stderr.strip()[:200]}")
else:
    warn("node not found — JS syntax check skipped")

print(f"\n=== VALIDATION: {len(passed)} passed, {len(warnings)} warnings, {len(errors)} errors ===")
for w in warnings:
    print("WARN:", w)
for e in errors:
    print("ERROR:", e)
sys.exit(1 if errors else 0)
