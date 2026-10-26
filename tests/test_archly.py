from pathlib import Path

from evalathan.evalers.archly import run
from evalathan.evalers.principles97 import infer
from evalathan.model import Status
from evalathan.subject import load


def test_empty_tree_is_not_a_review(tmp_path: Path) -> None:
    cell = run(load(tmp_path))
    assert cell.status is Status.DEFERRED
    assert cell.passed is None
    assert "Nothing to review" in cell.summary


def test_readme_evidence_scores_only_the_principles_it_cites(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "Requirements for the bridge are listed.\nLatency budget is 40 ms.\n",
        encoding="utf-8",
    )
    cell = run(load(tmp_path))
    assert cell.status is Status.SCORED
    assert cell.passed is None
    assert "97-principle review ran" in cell.summary
    assert "had citable evidence" in cell.summary
    assert "not counted as zero" in cell.summary
    assert "No gate pass is awarded." in cell.summary
    assert "3.59" not in cell.summary


def test_a_document_and_a_test_can_score_without_copying_a_foreign_card(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "architecture.md").write_text(
        "Architectural tradeoff: the relay keeps one process.\n",
        encoding="utf-8",
    )
    (tmp_path / "test_relay.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    rows = infer(
        [("docs/architecture.md", "architectural tradeoff: the relay keeps one process.\n", "doc")],
        ["docs/architecture.md", "test_relay.py"],
        lang_count=1,
        commit_count=None,
    )
    by_n = {row.n: row for row in rows}
    assert by_n[22].score == 3
    assert by_n[22].cite == "docs/architecture.md"
    assert by_n[15].score == 3
    assert by_n[1].score is None
    assert len(rows) == 97
