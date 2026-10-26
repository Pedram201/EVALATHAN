#!/bin/bash
set -e
cd "$(dirname "$0")"

if [ -x /opt/homebrew/bin/brew ]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
elif [ -x /usr/local/bin/brew ]; then
  eval "$(/usr/local/bin/brew shellenv)"
fi

has_window() {
  "$1" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)' >/dev/null 2>&1 \
    && "$1" -c 'import tkinter' >/dev/null 2>&1
}

find_python() {
  local candidate
  for candidate in python3 \
    /opt/homebrew/bin/python3 \
    /usr/local/bin/python3 \
    /Library/Frameworks/Python.framework/Versions/Current/bin/python3
  do
    if [ -x "$candidate" ] || command -v "$candidate" >/dev/null 2>&1; then
      if has_window "$candidate"; then
        command -v "$candidate"
        return 0
      fi
    fi
  done
  local framework
  for framework in /Library/Frameworks/Python.framework/Versions/*/bin/python3; do
    [ -x "$framework" ] || continue
    if has_window "$framework"; then
      echo "$framework"
      return 0
    fi
  done
  return 1
}

BASE=""
if BASE="$(find_python)"; then
  :
else
  if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3.10 or newer was not found."
    echo "Install it from https://www.python.org/downloads/macos/"
    exit 1
  fi
  VER="$(python3 -c 'import sys; print("%d.%d" % (sys.version_info.major, sys.version_info.minor))')"
  if command -v brew >/dev/null 2>&1; then
    echo "Python ${VER} has no window library (tkinter)."
    echo "Installing python-tk@${VER} ..."
    brew install "python-tk@${VER}"
  else
    echo "Python ${VER} has no window library (tkinter)."
    echo "Install Python from https://www.python.org/downloads/macos/ and run bash launch.sh again."
    exit 1
  fi
  if ! BASE="$(find_python)"; then
    echo "The window library is still missing after python-tk@${VER}."
    exit 1
  fi
fi

if [ -x .venv/bin/python ] && ! .venv/bin/python -c 'import tkinter' >/dev/null 2>&1; then
  rm -rf .venv
fi

if [ ! -x .venv/bin/python ]; then
  "$BASE" -m venv .venv
fi

. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
exec evalathan
