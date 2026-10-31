from pathlib import Path

from evalathan.dehydrus import conduct
from evalathan.hydra import conduct as hydra_conduct
from evalathan.model import Status


def test_empty_tree_lists_seven_deferrals(tmp_path: Path) -> None:
    report = conduct(tmp_path)
    assert len(report.cells) == 7
    assert report.passed == []
    assert "Evalathan v0.3" in report.render()
    assert report.to_dict()["conductor"] == "Dehydrus"
    assert report.habtwin == "No HabTwin lab trace"
    names = [cell.agent for cell in report.cells]
    assert names == [
        "Copernly",
        "Keplerly",
        "Galileoly",
        "Darwinly",
        "Mendly",
        "Einsteinly",
        "Newtonly",
    ]
    assert all(cell.status is Status.DEFERRED for cell in report.cells)
    assert "apple" in next(c for c in report.cells if c.agent == "Newtonly").summary


def test_hydra_stays_sixteen(tmp_path: Path) -> None:
    report = hydra_conduct(tmp_path)
    assert len(report.cells) == 16
    assert "Copernly" not in {cell.agent for cell in report.cells}


def test_sealed_galileo_is_measured_not_a_gold_medal(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("physical-world discovery agent\n", encoding="utf-8")
    (tmp_path / "ludats-g-trace.jsonl").write_text('{"step":1}\n', encoding="utf-8")
    report = conduct(tmp_path)
    by_name = {cell.agent: cell for cell in report.cells}
    assert by_name["Galileoly"].status is Status.SCORED
    assert by_name["Galileoly"].passed is None
    assert "gold medal is not awarded" in by_name["Galileoly"].summary
    assert by_name["Newtonly"].status is Status.DEFERRED
    assert by_name["Copernly"].status is Status.DEFERRED


def test_newton_waits_until_kepler_and_galileo(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("LuDaTs physical world\n", encoding="utf-8")
    (tmp_path / "ludats-k-trace.jsonl").write_text('{"step":1}\n', encoding="utf-8")
    (tmp_path / "ludats-g-trace.jsonl").write_text('{"step":1}\n', encoding="utf-8")
    (tmp_path / "ludats-n-trace.jsonl").write_text('{"step":1}\n', encoding="utf-8")
    report = conduct(tmp_path)
    by_name = {cell.agent: cell for cell in report.cells}
    assert by_name["Keplerly"].status is Status.SCORED
    assert by_name["Galileoly"].status is Status.SCORED
    assert by_name["Newtonly"].status is Status.SCORED


def test_habtwin_note_finds_lab_trace_only(tmp_path: Path) -> None:
    (tmp_path / "habtwin-notes.md").write_text("not a trace\n", encoding="utf-8")
    assert conduct(tmp_path).habtwin == "No HabTwin lab trace"
    (tmp_path / "habtwin-p-trace.jsonl").write_text('{"step":1}\n', encoding="utf-8")
    assert "habtwin-p-trace.jsonl" in conduct(tmp_path).habtwin
