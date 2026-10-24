"""Repository readiness checks."""

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, List


@dataclass(frozen=True)
class CheckResult:
    name: str
    passed: bool
    detail: str


def _exists(root: Path, *paths: str) -> bool:
    return any((root / path).exists() for path in paths)


def run_checks(root: Path) -> List[CheckResult]:
    checks: List[tuple[str, Callable[[Path], bool], str]] = [
        ("README", lambda path: _exists(path, "README", "README.md", "README.rst"), "Add a README describing the project."),
        ("License", lambda path: _exists(path, "LICENSE", "LICENSE.md", "LICENSE.txt"), "Add an OSI-approved LICENSE file."),
        ("Contributing guide", lambda path: _exists(path, "CONTRIBUTING.md", ".github/CONTRIBUTING.md"), "Add CONTRIBUTING.md with the development workflow."),
        ("Code of conduct", lambda path: _exists(path, "CODE_OF_CONDUCT.md", ".github/CODE_OF_CONDUCT.md"), "Add a CODE_OF_CONDUCT.md."),
        ("Security policy", lambda path: _exists(path, "SECURITY.md", ".github/SECURITY.md"), "Add SECURITY.md with vulnerability reporting guidance."),
        ("Issue or PR templates", lambda path: _exists(path, ".github/ISSUE_TEMPLATE", ".github/PULL_REQUEST_TEMPLATE.md"), "Add an issue template or pull-request template."),
        ("Continuous integration", lambda path: _exists(path, ".github/workflows", ".gitlab-ci.yml", ".circleci/config.yml"), "Add a CI workflow that runs checks on changes."),
    ]
    return [
        CheckResult(name, passed := check(root), "OK" if passed else detail)
        for name, check, detail in checks
    ]


def as_json(results: List[CheckResult]) -> List[Dict[str, object]]:
    return [asdict(result) for result in results]
