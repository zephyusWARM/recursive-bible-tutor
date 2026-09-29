#!/usr/bin/env python3
"""Small dependency-free validation for the required Agent Skills frontmatter."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def main() -> int:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit("SKILL.md must begin with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit("SKILL.md frontmatter is not closed")
    frontmatter = text[4:end]
    fields = {}
    for line in frontmatter.splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise SystemExit(f"invalid skill name: {name!r}")
    if len(name) > 64:
        raise SystemExit("skill name exceeds 64 characters")
    if not description or len(description) > 1024:
        raise SystemExit("description must be 1..1024 characters")
    if name != ROOT.name:
        raise SystemExit(f"skill name {name!r} must match directory {ROOT.name!r}")

    print("OK: core Agent Skills metadata is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
