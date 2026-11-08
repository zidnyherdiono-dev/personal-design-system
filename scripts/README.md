# Scripts

| Script | Purpose |
|---|---|
| `serve.py` | Local preview server (default http://localhost:8080, override with `PDS_PORT`) |
| `validate.py` | Repo validator: structure, docs standard, catalog sync, links, tokens, HTML/JS sanity |

Run validation before committing structural changes:

```bash
python scripts/validate.py
```
