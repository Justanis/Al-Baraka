# --------------------------------------------------------------------------------
# This script will:
#   1. Check if a virtual environment folder (venv) exists; if not, create one.
#   2. Activate the virtual environment.
#   3. Upgrade pip and install Flask (or other requirements).
#   4. Run the Flask app.
# --------------------------------------------------------------------------------

# Ensure we are in the same directory as this script
Set-Location $PSScriptRoot

# 1. Check if 'venv' folder exists, if not create it
if (!(Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# 2. Activate the virtual environment in PowerShell
Write-Host "Activating virtual environment..."
. .\venv\Scripts\activate

# 3. Upgrade pip and install Flask
Write-Host "Upgrading pip and installing Flask..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Run the Flask app
Write-Host "Running Flask app..."
python app.py

# Optional: pause so the window stays open if double-clicked
Write-Host "`nPress Enter to exit..."
[void][System.Console]::ReadKey($true)
