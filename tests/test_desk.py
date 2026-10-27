import pytest

from evalathan.desk import add_heading, checkout_name, classify, place_logo, prepare


def test_blank_paste_is_refused() -> None:
    with pytest.raises(ValueError, match="Paste"):
        classify("  ")


def test_github_link_is_not_a_folder() -> None:
    kind, url = classify("https://github.com/python/cpython.git")
    assert kind == "github"
    assert checkout_name(url) == "python__cpython"


def test_local_folder_is_used_as_itself(tmp_path) -> None:
    folder, note = prepare(str(tmp_path))
    assert folder == tmp_path
    assert note == ""


def test_missing_folder_is_refused(tmp_path) -> None:
    with pytest.raises(ValueError, match="not found"):
        prepare(str(tmp_path / "missing"))


def test_logo_sits_between_browse_and_evaluate() -> None:
    tk = pytest.importorskip("tkinter")
    from tkinter import ttk

    root = tk.Tk()
    root.withdraw()
    try:
        frame = ttk.Frame(root)
        add_heading(frame, root)
        assert frame.winfo_children()[0].cget("text") == "HYDRA"
        row = ttk.Frame(frame)
        ttk.Button(row, text="Browse folder").pack(side="left")
        place_logo(row, root)
        ttk.Button(row, text="Evaluate").pack(side="left")
        browse, logo, evaluate = row.winfo_children()
        assert browse.cget("text") == "Browse folder"
        assert logo.cget("image")
        assert evaluate.cget("text") == "Evaluate"
        assert root._hydra_mark.width() >= 96
    finally:
        root.destroy()
