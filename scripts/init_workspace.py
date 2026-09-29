#!/usr/bin/env python3
"""Initialize a persistent learning workspace from bundled templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

TEMPLATES = [
    "TOPIC.md",
    "KNOWLEDGE_GRAPH.md",
    "LEARNER_STATE.md",
    "MISCONCEPTIONS.md",
    "REVIEW_QUEUE.md",
    "SESSION_LOG.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize Recursive Bible Tutor learning state.")
    parser.add_argument("directory", help="Destination directory for the learning workspace")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    template_dir = skill_root / "assets" / "templates"
    destination = Path(args.directory).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    for name in TEMPLATES:
        src = template_dir / name
        dst = destination / name
        if dst.exists() and not args.force:
            print(f"skip: {dst} already exists")
            continue
        shutil.copyfile(src, dst)
        print(f"created: {dst}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
