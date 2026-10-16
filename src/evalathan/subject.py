"""What Hydra can see: files on disk, not a claim in a sentence."""

from __future__ import annotations

import subprocess
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    "dist",
    "build",
    ".mypy_cache",
}
EXT_LANG = {
    ".py": "Python",
    ".pyi": "Python",
    ".js": "JavaScript",
    ".mjs": "JavaScript",
    ".cjs": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript",
    ".jsx": "JavaScript",
    ".c": "C",
    ".h": "C",
    ".cc": "C++",
    ".cpp": "C++",
    ".cxx": "C++",
    ".hpp": "C++",
    ".rs": "Rust",
    ".go": "Go",
    ".java": "Java",
    ".kt": "Kotlin",
    ".rb": "Ruby",
    ".php": "PHP",
    ".cs": "C#",
    ".swift": "Swift",
    ".mel": "MEL",
    ".vfl": "VEX",
}
MAX_FILES = 8000
PRIORITY_NAMES = {
    "4uvals.json",
    "agent_registry.md",
    "agents.md",
    "leviathan_v1.json",
    "eval_leviathan.md",
}
README_NAMES = {"readme.md", "readme.txt", "readme.rst", "readme"}


@dataclass
class Subject:
    root: Path
    files: list[Path] = field(default_factory=list)
    by_lang: dict[str, int] = field(default_factory=dict)
    readme_text: str = ""
    commit_count: int | None = None
    truncated: bool = False

    def rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.root))
        except ValueError:
            return str(path)

    def named(self, filename: str) -> list[Path]:
        needle = filename.lower()
        return [p for p in self.files if p.name.lower() == needle]

    def text_hits(self, *needles: str) -> list[str]:
        blob = self.readme_text.lower()
        return [n for n in needles if n.lower() in blob]


def _git_count(root: Path) -> int | None:
    if not (root / ".git").exists():
        return None
    try:
        out = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=root,
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0:
        return None
    try:
        return int(out.stdout.strip())
    except ValueError:
        return None


def load(root: Path) -> Subject:
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)
    files: list[Path] = []
    truncated = False
    seen: set[Path] = set()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name.lower() not in PRIORITY_NAMES and "fuss" not in path.name.lower():
            continue
        files.append(path)
        seen.add(path)
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file() or path in seen:
            continue
        files.append(path)
        if len(files) >= MAX_FILES:
            truncated = True
            break
    counts: Counter[str] = Counter()
    for path in files:
        lang = EXT_LANG.get(path.suffix.lower())
        if lang:
            counts[lang] += 1
    readme = ""
    for path in files:
        if path.name.lower() in README_NAMES:
            try:
                readme = path.read_text(encoding="utf-8", errors="replace")[:20000]
            except OSError:
                readme = ""
            break
    return Subject(
        root=root,
        files=files,
        by_lang=dict(counts.most_common()),
        readme_text=readme,
        commit_count=_git_count(root),
        truncated=truncated,
    )
