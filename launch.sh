#!/bin/bash
set -e
cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.10 or newer was not found."
  echo "Install it from https://www.python.org/downloads/macos/"
  exit 1
fi

if ! python3 -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'; then
  echo "Python 3.10 or newer is required."
  echo "Install it from https://www.python.org/downloads/macos/"
  exit 1
fi

if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
fi

. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .

if ! python -c 'import tkinter' >/dev/null 2>&1; then
  echo "This Python has no window library (tkinter)."
  echo "Install Python 3.10 or newer from https://www.python.org/downloads/macos/"
  exit 1
fi

exec evalathan
