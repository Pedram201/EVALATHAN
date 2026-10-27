"""A small window: paste a GitHub link or a folder, then evaluate it."""

from __future__ import annotations

import re
import subprocess
import threading
from pathlib import Path

from evalathan.hydra import conduct

_GITHUB = re.compile(
    r"^https?://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+?)(?:\.git)?(?:/.*)?$",
    re.IGNORECASE,
)


def classify(text: str) -> tuple[str, str]:
    """Return ('github', url) or ('path', text). Empty text is refused."""
    raw = text.strip().strip('"')
    if not raw:
        raise ValueError("Paste a GitHub link or a folder on this PC.")
    if _GITHUB.match(raw):
        return "github", raw
    return "path", raw


def checkout_name(url: str) -> str:
    match = _GITHUB.match(url.strip())
    if not match:
        raise ValueError("That is not a github.com link to a repository.")
    owner = match.group("owner")
    repo = match.group("repo")
    if owner in {".", ".."} or repo in {".", ".."}:
        raise ValueError("That GitHub link is not a repository.")
    return f"{owner}__{repo}"


def prepare(text: str, scans: Path | None = None) -> tuple[Path, str]:
    """Turn a pasted link or folder into a directory Hydra can read."""
    kind, raw = classify(text)
    if kind == "path":
        folder = Path(raw).expanduser()
        if not folder.is_dir():
            raise ValueError(f"That folder was not found: {folder}")
        return folder, ""
    root = scans if scans is not None else Path.home() / "evalathan-scans"
    root.mkdir(parents=True, exist_ok=True)
    dest = root / checkout_name(raw)
    if (dest / ".git").is_dir():
        return dest, f"Using the copy already downloaded at {dest}"
    try:
        subprocess.run(
            ["git", "clone", raw, str(dest)],
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise ValueError(
            "Git is not installed, so a GitHub link cannot be downloaded. "
            "Paste a folder on this PC, or install Git for Windows."
        ) from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        raise ValueError(detail or "Git could not download that repository.") from exc
    return dest, f"Downloaded to {dest}"


def add_heading(frame, root) -> None:
    """HYDRA at the left. The mark sits at the top-right corner."""
    import tkinter as tk
    from tkinter import ttk

    head = ttk.Frame(frame)
    head.pack(fill="x")
    ttk.Label(head, text="HYDRA", font=("Segoe UI", 18, "bold")).pack(side="left", anchor="n")
    logo_path = Path(__file__).with_name("hydra-logo.png")
    if not logo_path.is_file():
        return
    image = tk.PhotoImage(file=str(logo_path))
    step = max(1, round(image.width() / 56))
    shown = image.subsample(step, step) if step > 1 else image
    root.iconphoto(True, shown)
    root._hydra_logo = image
    root._hydra_mark = shown
    ttk.Label(head, image=shown).pack(side="right", anchor="n")


def open_desk() -> int:
    import tkinter as tk
    from tkinter import filedialog, messagebox, scrolledtext, ttk

    root = tk.Tk()
    root.title("HYDRA")
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
        chosen = filedialog.askdirectory(title="Choose the software folder")
        if chosen:
            pasted.set(chosen)

    def save() -> None:
        body = report.get("1.0", "end").strip()
        if not body:
            messagebox.showinfo("HYDRA", "There is no report to save yet.")
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
