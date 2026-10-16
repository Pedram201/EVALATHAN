import json
from pathlib import Path

from evalathan.hydra import conduct
from evalathan.model import Status


def test_4uvals_record_is_a_levi_pass(tmp_path: Path) -> None:
    (tmp_path / "4uvals.json").write_text(
        json.dumps({"family": "4Uvals", "gate": {"mean": 3.4, "result": "PASS"}}),
        encoding="utf-8",
    )
    cell = next(c for c in conduct(tmp_path).cells if c.agent == "Levi")
    assert cell.status is Status.SCORED
    assert cell.passed is True
    assert "3.4" in cell.summary


def test_tokex_pair_reports_savings_including_a_legal_zero(tmp_path: Path) -> None:
    (tmp_path / "meter.json").write_text(
        json.dumps({"tokex": {"total_tokex": 10, "tokex_this_run": 10}}),
        encoding="utf-8",
    )
    cell = next(c for c in conduct(tmp_path).cells if c.agent == "Tokly")
    assert cell.status is Status.SCORED
    assert "savings 0" in cell.summary


def test_fuss_file_passes_menschly_only(tmp_path: Path) -> None:
    (tmp_path / "fuss.py").write_text("def bind_fuss():\n    return 25\n", encoding="utf-8")
    cells = {c.agent: c for c in conduct(tmp_path).cells}
    assert cells["Menschly"].passed is True
    assert cells["Levi"].passed is not True


def test_question_bank_is_counted(tmp_path: Path) -> None:
    (tmp_path / "questions.json").write_text(
        json.dumps([{"id": "q1"}, {"id": "q2"}]),
        encoding="utf-8",
    )
    cell = next(c for c in conduct(tmp_path).cells if c.agent == "Domly")
    assert cell.status is Status.SCORED
    assert "2 questions" in cell.summary
