import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"  # Removed the extra space before 'test.py'
]

# Loop through each file in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir = filepath.parent  # Extract directory

    # Create directory if it doesn't exist
    if filedir and not filedir.exists():
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"✅ Created directory: {filedir}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass  # Creates an empty file
        logging.info(f"📝 Created empty file: {filepath}")
    else:
        logging.info(f"📂 {filepath} already exists")

# Verification
print("\n🔎 Verifying created files:")
for filepath in list_of_files:
    filepath = Path(filepath)
    if filepath.exists():
        print(f"✅ {filepath} exists")
    else:
        print(f"❌ {filepath} NOT found")
