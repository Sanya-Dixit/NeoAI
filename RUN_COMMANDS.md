# Run Commands for YourAI (Neo)

This file contains copyable commands for running the project in different modes from a Windows PowerShell terminal. Replace paths if your virtual environment or files are located elsewhere.

## Activate virtual environment (PowerShell)
.
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

## Run Online Mode (uses `main.py`)
```
.\.venv\Scripts\python.exe main.py
```

## Run Offline Mode (uses `neo_offline.py`)
```
.\.venv\Scripts\python.exe neo_offline.py
```

## Run Menu (batch menu)
```
.
./run_neo_menu.bat
```

## Quick test (OpenAI API connection)
```
.\.venv\Scripts\python.exe quick_test.py
```

## Install dependencies
```
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run using the PowerShell helper script
```
# run in PowerShell from repo root:
.
./run_mode.ps1 -Mode offline
```

Notes
- If PowerShell execution policy blocks running `run_mode.ps1`, use the `Set-ExecutionPolicy` command above or run it with `powershell -ExecutionPolicy Bypass -File .\run_mode.ps1 -Mode offline`.
- If your venv path differs, update the `.venv\Scripts\python.exe` path accordingly.
