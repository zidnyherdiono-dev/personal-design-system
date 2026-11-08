#!/usr/bin/env python3
"""Serve the design system preview locally (zero build step)."""
import http.server
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("PDS_PORT", "8080"))

if __name__ == "__main__":
    os.chdir(ROOT)
    print(f"Personal Design System preview: http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(
        ("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler
    ).serve_forever()
