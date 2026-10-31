"""A small window for Dehydrus. Paste a GitHub link or a folder, then evaluate it."""

from __future__ import annotations

import threading
from pathlib import Path

from evalathan.dehydrus import conduct
from evalathan.desk import prepare


def add_heading(frame, root) -> None:
    """DEHYDRUS at the left. The mark sits at the top-right corner."""
    import tkinter as tk
    from tkinter import ttk

    head = ttk.Frame(frame)
    head.pack(fill="x")
    ttk.Label(head, text="DEHYDRUS", font=("Segoe UI", 18, "bold")).pack(side="left")
    logo_path = Path(__file__).with_name("dehydrus-logo.png")
    if not logo_path.is_file():
        return
    image = tk.PhotoImage(file=str(logo_path))
    step = max(1, round(image.height() / round(56 * 1.12 * 1.16 * 1.11)))
    shown = image.subsample(step, step) if step > 1 else image
    root.iconphoto(True, shown)
    root._dehydrus_logo = image
    root._dehydrus_mark = shown
    ttk.Label(head, image=shown).pack(side="right")


def open_desk() -> int:
    import tkinter as tk
    from tkinter import filedialog, messagebox, scrolledtext, ttk

    root = tk.Tk()
    root.title("DEHYDRUS")
    root.geometry("760x560")
    root.minsize(640, 420)

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    add_heading(frame, root)
    ttk.Label(
        frame,
        text="Paste a GitHub link, or a folder on this PC. Then press Evaluate.",
    ).pack(anchor="w", pady=(0, 10))

    row = ttk.Frame(frame)
    row.pack(fill="x")
    pasted = tk.StringVar()
    entry = ttk.Entry(row, textvariable=pasted)
    entry.pack(side="left", fill="x", expand=True)
    entry.focus_set()

    report = scrolledtext.ScrolledText(frame, wrap="word", font=("Consolas", 10))
    report.pack(fill="both", expand=True, pady=(12, 8))
    status = tk.StringVar(value="Waiting.")
    ttk.Label(frame, textvariable=status).pack(anchor="w")

    busy = {"on": False}

    def show(body: str, note: str) -> None:
        busy["on"] = False
        evaluate_button.state(["!disabled"])
        report.delete("1.0", "end")
        report.insert("1.0", body)
        status.set(note or "Done.")

    def evaluate() -> None:
        if busy["on"]:
            return
        text = pasted.get()
        busy["on"] = True
        evaluate_button.state(["disabled"])
        status.set("Evaluating. A GitHub link is downloaded first.")

        def work() -> None:
            try:
                folder, note = prepare(text)
                body = conduct(folder).render()
                if note:
                    body = note + "\n\n" + body
                root.after(0, lambda: show(body, "Done."))
            except Exception as exc:
                message = str(exc) or exc.__class__.__name__
                root.after(0, lambda: show(message, "Stopped."))

        threading.Thread(target=work, daemon=True).start()

    def browse() -> None:
        chosen = filedialog.askdirectory(title="Choose the folder")
        if chosen:
            pasted.set(chosen)

    def save() -> None:
        body = report.get("1.0", "end").strip()
        if not body:
            messagebox.showinfo("DEHYDRUS", "There is no report to save yet.")
            return
        target = filedialog.asksaveasfilename(
            title="Save the report",
            defaultextension=".txt",
            filetypes=[("Text", "*.txt"), ("All files", "*.*")],
        )
        if target:
            Path(target).write_text(body + "\n", encoding="utf-8")
            status.set(f"Saved {target}")

    ttk.Button(row, text="Browse folder", command=browse).pack(side="left", padx=(8, 0))
    evaluate_button = ttk.Button(row, text="Evaluate", command=evaluate)
    evaluate_button.pack(side="left", padx=(8, 0))
    ttk.Button(frame, text="Save report", command=save).pack(anchor="e")

    root.bind("<Return>", lambda _event: evaluate())
    root.mainloop()
    return 0
