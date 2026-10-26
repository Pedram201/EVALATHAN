import json
from pathlib import Path

from evalathan.hydra import conduct
from evalathan.model import Status


def test_a_count_is_labeled_measured_not_scored(tmp_path: Path) -> None:
    (tmp_path / "widget.py").write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")
    report = conduct(tmp_path)
    rendered = report.render()
    codely = next(line for line in rendered.splitlines() if line.startswith("Codely"))
    assert "measured" in codely
    assert "scored" not in codely
    assert '"status": "scored"' not in json.dumps(report.to_dict())


def test_empty_tree_lists_deferrals_and_does_not_pass(tmp_path: Path) -> None:
    report = conduct(tmp_path)
    assert len(report.cells) == 16
    assert report.passed == []
    assert "deferred" in report.headline()
    blob = json.dumps(report.to_dict())
    assert "0.0" not in report.headline()
    assert "SOTA" not in blob


def test_python_pack_measures_branches_without_a_fake_pass(tmp_path: Path) -> None:
    (tmp_path / "widget.py").write_text(
        "def add(a, b):\n"
        "    if a and b:\n"
        "        return a + b\n"
        "    return 0\n",
        encoding="utf-8",
    )
    (tmp_path / "test_widget.py").write_text("def test_add():\n    assert True\n", encoding="utf-8")
    report = conduct(tmp_path)
    by_name = {cell.agent: cell for cell in report.cells}
    assert by_name["Codely"].status is Status.SCORED
    assert by_name["Codely"].passed is None
    assert "ISO/IEC 5055 were not run" in by_name["Codely"].summary
    assert by_name["Mixly"].status is Status.SCORED
    assert "Python" in by_name["Mixly"].summary
    assert "rewrite" in by_name["Mixly"].summary
    assert by_name["Stackly"].status is Status.SCORED
    assert "does not blend" in by_name["Stackly"].summary
    assert by_name["Runly"].status is Status.SCORED
    assert "microbench" in by_name["Runly"].summary


def test_identical_bytes_are_a_refactorly_fact(tmp_path: Path) -> None:
    (tmp_path / "a.py").write_text("x = 1\n", encoding="utf-8")
    (tmp_path / "b.py").write_text("x = 1\n", encoding="utf-8")
    report = conduct(tmp_path)
    cell = next(c for c in report.cells if c.agent == "Refactorly")
    assert cell.status is Status.SCORED
    assert "1 identical-byte" in cell.summary


def test_unknown_language_is_not_a_codely_pass(tmp_path: Path) -> None:
    (tmp_path / "notes.mel").write_text("print(1);\n", encoding="utf-8")
    report = conduct(tmp_path)
    cell = next(c for c in report.cells if c.agent == "Codely")
    assert cell.status is Status.DEFERRED
    assert cell.passed is None
    assert "not a pass" in cell.summary


def test_naming_m3_is_not_a_declared_order(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "Triadly records an M3 order (cost, speed, impact).\n",
        encoding="utf-8",
    )
    report = conduct(tmp_path)
    cell = next(c for c in report.cells if c.agent == "Triadly")
    assert cell.status is Status.DEFERRED


def test_detector_source_is_not_a_menschly_timer(tmp_path: Path) -> None:
    (tmp_path / "menschly.py").write_text(
        'TIMER_MARKS = ("session_limit_minutes",)\n',
        encoding="utf-8",
    )
    report = conduct(tmp_path)
    cell = next(c for c in report.cells if c.agent == "Menschly")
    assert cell.passed is not True


def test_stop_language_does_not_require_fuss(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "Session limit: leave after twenty five minutes.\n",
        encoding="utf-8",
    )
    report = conduct(tmp_path)
    cell = next(c for c in report.cells if c.agent == "Menschly")
    assert cell.status is Status.PROVISIONAL
    assert cell.passed is None
