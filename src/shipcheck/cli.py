"""Command-line entry point for ShipCheck."""

import argparse
import json
from pathlib import Path
from typing import Optional, Sequence

from .checks import as_json, run_checks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check whether a repository is ready to ship as open source.")
    parser.add_argument("path", nargs="?", default=".", type=Path, help="Repository path (default: current directory).")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Print machine-readable JSON.")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.path.resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}")
        return 2

    results = run_checks(root)
    if args.json_output:
        print(json.dumps({"path": str(root), "passed": all(item.passed for item in results), "checks": as_json(results)}, indent=2))
    else:
        print(f"ShipCheck: {root}")
        for result in results:
            marker = "PASS" if result.passed else "FAIL"
            print(f"[{marker}] {result.name}: {result.detail}")
        print("Ready to ship." if all(item.passed for item in results) else "Not ready to ship yet.")
    return 0 if all(item.passed for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

