#!/bin/bash

# Ensure the script stops on first error
set -e

# Activate virtual environment
echo "Activating virtual environment..."
source virtual_enviroment/bin/activate

# Navigate to the application directory (adjust if your main.py is located in a different folder)
echo "Navigating to the application directory..."

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/

# Generate binary using PyInstaller
echo "Generating application binary with PyInstaller..."
pyinstaller --onefile --clean --name app_vehicles run.py

# Deactivate virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Binary generation completed successfully. Check the dist/ directory."