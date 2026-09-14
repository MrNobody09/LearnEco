"""Validate that required LearnEco repository artifacts are present."""

from pathlib import Path


REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "docs/current-state.md",
    "docs/documentation-rules.md",
    "docs/workflow.md",
    "docs/open-questions.md",
)
REQUIRED_DIRECTORIES = ("docs/decisions",)


def find_missing_artifacts(repository_root: Path) -> list[str]:
    """Return required artifact paths that are absent or have the wrong type."""
    missing_files = [
        path for path in REQUIRED_FILES if not (repository_root / path).is_file()
    ]
    missing_directories = [
        path
        for path in REQUIRED_DIRECTORIES
        if not (repository_root / path).is_dir()
    ]
    return missing_files + missing_directories


def main() -> int:
    missing_artifacts = find_missing_artifacts(Path.cwd())

    if missing_artifacts:
        print("Repository health check failed. Missing required artifacts:")
        for artifact in missing_artifacts:
            print(f"- {artifact}")
        return 1

    print("Repository health check passed: all required artifacts are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
