import tempfile
import unittest
from pathlib import Path

from shipcheck.checks import run_checks


class RunChecksTests(unittest.TestCase):
    def test_empty_repository_fails_all_checks(self):
        with tempfile.TemporaryDirectory(dir=".") as directory:
            results = run_checks(Path(directory))
        self.assertEqual(len(results), 7)
        self.assertTrue(all(not result.passed for result in results))

    def test_repository_with_expected_files_passes(self):
        with tempfile.TemporaryDirectory(dir=".") as directory:
            root = Path(directory)
            for path in (
                "README.md",
                "LICENSE",
                "CONTRIBUTING.md",
                "CODE_OF_CONDUCT.md",
                "SECURITY.md",
                ".github/ISSUE_TEMPLATE/bug.yml",
                ".github/workflows/ci.yml",
            ):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
            results = run_checks(root)
        self.assertTrue(all(result.passed for result in results))


if __name__ == "__main__":
    unittest.main()

