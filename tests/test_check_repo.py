import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.check_repo import REQUIRED_DIRECTORIES, REQUIRED_FILES


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "check_repo.py"


class RepositoryHealthCheckTests(unittest.TestCase):
    def create_repository(self, root: Path) -> None:
        for relative_path in REQUIRED_FILES:
            artifact = root / relative_path
            artifact.parent.mkdir(parents=True, exist_ok=True)
            artifact.touch()
        for relative_path in REQUIRED_DIRECTORIES:
            (root / relative_path).mkdir(parents=True, exist_ok=True)

    def run_check(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            cwd=root,
            capture_output=True,
            check=False,
            text=True,
        )

    def test_succeeds_when_all_required_artifacts_are_present(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository_root = Path(directory)
            self.create_repository(repository_root)

            result = self.run_check(repository_root)

        self.assertEqual(result.returncode, 0)
        self.assertIn("Repository health check passed", result.stdout)

    def test_reports_missing_artifact_and_exits_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository_root = Path(directory)
            self.create_repository(repository_root)
            (repository_root / "docs" / "workflow.md").unlink()

            result = self.run_check(repository_root)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Repository health check failed", result.stdout)
        self.assertIn("docs/workflow.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
