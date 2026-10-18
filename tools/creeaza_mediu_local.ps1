# Creează un mediu Python local pentru curs în folderul .venv al repository-ului.
# Folosire (PowerShell, din folderul SEED):  .\tools\creeaza_mediu_local.ps1
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$venv = Join-Path $repo '.venv'

Write-Host "Se creează mediul virtual în $venv ..."
python -m venv $venv
& "$venv\Scripts\python.exe" -m pip install --upgrade pip
& "$venv\Scripts\python.exe" -m pip install -r (Join-Path $repo 'requirements-local.txt')
& "$venv\Scripts\python.exe" -m ipykernel install --user --name seed --display-name "Python (SEED)"

Write-Host ""
Write-Host "Gata. În VS Code: Command Palette -> Python: Select Interpreter -> .venv (sau kernelul 'Python (SEED)')."
