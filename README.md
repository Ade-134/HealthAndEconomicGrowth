# 1. Install venv (if not already installed)
## (venv is included by default in Python 3.3+)
## For Debian/Ubuntu systems, you may need to run:
sudo apt install python3-venv

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
## On Linux/macOS:
source venv/bin/activate

## On Windows (cmd):
venv\Scripts\activate

## On Windows (PowerShell):
venv\Scripts\Activate.ps1

# 4. Install dependencies from requirements.txt
pip install -r requirements.txt