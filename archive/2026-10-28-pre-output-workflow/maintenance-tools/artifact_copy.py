#!/usr/bin/env python3
"""Make a publish-ready copy of a standalone study page for the Artifact tool.

The Artifact viewer wraps the page in its own <!doctype>/<html>/<head>/<body>
skeleton, so this strips those wrapper tags (and the charset/viewport metas)
and leaves <title>, <style>, content and <script> in order.

Usage: python3 scripts/artifact_copy.py <page.html> <out.html>
"""
import re
import sys

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
for pat in [
    r"<!DOCTYPE html>\s*",
    r"<!--.*?-->\s*(?=<html)",
    r"<html[^>]*>\s*",
    r"<head>\s*",
    r'<meta charset="[^"]*">\s*',
    r'<meta name="viewport"[^>]*>\s*',
    r"</head>\s*",
    r"<body[^>]*>\s*",
    r"</body>\s*",
    r"</html>\s*",
]:
    s = re.sub(pat, "", s, count=1, flags=re.I | re.S)
open(out, "w", encoding="utf-8").write(s)
print(f"wrote {out}")
