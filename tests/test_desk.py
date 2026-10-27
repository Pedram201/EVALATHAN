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


def test_logo_sits_above_browse_and_evaluate() -> None:
    tk = pytest.importorskip("tkinter")
    from tkinter import ttk

    root = tk.Tk()
    root.withdraw()
    try:
        frame = ttk.Frame(root)
        add_heading(frame, root)
        assert frame.winfo_children()[0].cget("text") == "HYDRA"
        actions = ttk.Frame(frame)
        place_logo(actions, root)
        buttons = ttk.Frame(actions)
        buttons.pack(side="top")
        ttk.Button(buttons, text="Browse folder").pack(side="left")
        ttk.Button(buttons, text="Evaluate").pack(side="left")
        logo, button_row = actions.pack_slaves()
        assert logo.cget("image")
        assert button_row.winfo_children()[0].cget("text") == "Browse folder"
        assert button_row.winfo_children()[1].cget("text") == "Evaluate"
        assert root._hydra_mark.width() >= 96
    finally:
        root.destroy()
