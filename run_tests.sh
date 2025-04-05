#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Echo commands
set -x

# Check if virtual environment exists and activate it
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install dependencies
python -m pip install --upgrade pip
pip install -e .
pip install pytest pytest-cov

# Check for Python unit tests
if [ -d "kybra_simple_shell/tests/" ]; then
    echo "Running Python unit tests..."
    python -m pytest kybra_simple_shell/tests/
else
    echo "No Python tests directory found at kybra_simple_shell/tests/"
    echo "Current directory contents:"
    ls -la
    echo "\nkybra_simple_shell directory contents:"
    ls -la kybra_simple_shell/ || echo "kybra_simple_shell/ not found"
    exit 1
fi

echo "✅ All unit tests passed successfully!"
