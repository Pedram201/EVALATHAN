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
        row = ttk.Frame(frame)
        row.columnconfigure(0, weight=1)
        entry = ttk.Entry(row)
        entry.grid(row=1, column=0, sticky="ew")
        place_logo(row, root, row=0, column=1, columnspan=2, pady=(0, 12))
        browse = ttk.Button(row, text="Browse folder")
        browse.grid(row=1, column=1, padx=(8, 0))
        evaluate = ttk.Button(row, text="Evaluate")
        evaluate.grid(row=1, column=2, padx=(8, 0))
        assert entry.grid_info()["row"] == browse.grid_info()["row"] == evaluate.grid_info()["row"]
        logo = row.grid_slaves(row=0, column=1)[0]
        assert logo.cget("image")
        assert int(logo.grid_info()["row"]) == 0
        assert logo.grid_info()["pady"] == (0, 12)
        assert root._hydra_mark.width() >= 96
    finally:
        root.destroy()
