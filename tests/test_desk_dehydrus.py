import pytest

from evalathan.desk_dehydrus import add_heading


def test_dehydrus_logo_sits_at_the_top_right() -> None:
    tk = pytest.importorskip("tkinter")
    from tkinter import ttk

    root = tk.Tk()
    root.withdraw()
    try:
        frame = ttk.Frame(root)
        add_heading(frame, root)
        name, logo = frame.winfo_children()[0].pack_slaves()
        assert name.cget("text") == "DEHYDRUS"
        assert name.pack_info()["side"] == "left"
        assert logo.cget("image")
        assert logo.pack_info()["side"] == "right"
    finally:
        root.destroy()
