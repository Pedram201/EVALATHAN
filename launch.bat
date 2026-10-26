@echo off
setlocal
cd /d "%~dp0"

set "PYLAUNCH="
py -3 -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 set "PYLAUNCH=py -3"
if not defined PYLAUNCH (
  python -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
  if not errorlevel 1 set "PYLAUNCH=python"
)
if not defined PYLAUNCH (
  echo Python 3.10 or newer was not found.
  echo Install it from https://www.python.org/downloads/windows/
  echo On the first installer page, tick Add python.exe to PATH.
  pause
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  %PYLAUNCH% -m venv .venv
  if errorlevel 1 (
    echo Could not create the private Python folder .venv
    pause
    exit /b 1
  )
)

call ".venv\Scripts\activate.bat"
python -m pip install -U pip
if errorlevel 1 (
  echo pip could not be updated.
  pause
  exit /b 1
)
python -m pip install -e .
if errorlevel 1 (
  echo Evalathan could not be installed.
  pause
  exit /b 1
)

evalathan
if errorlevel 1 pause
endlocal
