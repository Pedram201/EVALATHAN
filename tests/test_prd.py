import json
from pathlib import Path

from evalathan.evalers import ALL
from evalathan.hydra import conduct


def test_missing_prd_prints_no_prd_found_and_does_not_add_a_cell(tmp_path: Path) -> None:
    (tmp_path / "widget.py").write_text("x = 1\n", encoding="utf-8")
    report = conduct(tmp_path)
    assert len(report.cells) == 16
    assert len(ALL) == 16
    assert report.prd == "No PRD found"
    assert "No PRD found" in report.render()
    blob = json.dumps(report.to_dict())
    assert '"prd": "No PRD found"' in blob
    assert len(report.to_dict()["cells"]) == 16


def test_named_prd_file_is_printed_and_is_not_a_seventeenth_evaler(tmp_path: Path) -> None:
    (tmp_path / "PRD.md").write_text("The product must time a sitting.\n", encoding="utf-8")
    report = conduct(tmp_path)
    assert len(report.cells) == 16
    assert report.prd == "PRD found: PRD.md"
    assert "PRD found: PRD.md" in report.render()
    assert "No PRD found" not in report.render()


def test_prd_under_docs_counts_and_a_readme_sentence_does_not(tmp_path: Path) -> None:
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "product-requirements.md").write_text("Must, should, could.\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("This product has a PRD somewhere.\n", encoding="utf-8")
    (tmp_path / "prd-notes.md").write_text("Not the document.\n", encoding="utf-8")
    report = conduct(tmp_path)
    assert report.prd == "PRD found: docs/product-requirements.md"
    assert "prd-notes.md" not in report.prd
