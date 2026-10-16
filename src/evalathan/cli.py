"""evalathan scan <path>"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from evalathan.hydra import conduct


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="evalathan",
        description="Grade a software tree with Hydra. Blanks stay blank.",
    )
    parser.add_argument("command", choices=["scan"])
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    args = parser.parse_args(argv)
    try:
        report = conduct(args.path)
    except NotADirectoryError:
        print(f"Not a directory: {args.path}", file=sys.stderr)
        return 2
    print(report.render())
    if args.json_path:
        args.json_path.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
