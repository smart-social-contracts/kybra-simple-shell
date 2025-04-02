#!/bin/bash
set -e
set -x

# Start dfx in the background
echo "Starting dfx..."
dfx start --background --clean > src/log.txt 2>&1

# Deploy the test canister
echo "Deploying test canister..."
dfx deploy

# Get the canister ID
CANISTER_ID=$(dfx canister id test)
echo "Test canister ID: ${CANISTER_ID}"

# Install the kybra-simple-shell package for testing
echo "Installing Kybra Simple Shell..."
cd /app/src
# Create an __init__.py file to make the directory a package
touch __init__.py
cd kybra_simple_shell
# Install the package in development mode and ensure dependencies are installed
pip install -e .
# Make sure prompt_toolkit is installed
pip install prompt_toolkit>=3.0.0
# Add site-packages to PYTHONPATH for the test scripts
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.10/site-packages

# Test the shell by running some test commands
echo "Testing Kybra Simple Shell with the deployed canister..."

# The test files are now directly mounted to /app in the container

# Run the test script
cd /app  # Return to app root directory
python /app/test_shell_commands.py
TEST_RESULT=$?

# Create a simple functional test instead of running unit tests
echo "Running a simple functional test of the CLI tool..."

# CLI test file is directly mounted to /app

# Run the test
cd /app
PYTHONPATH=/app/src python cli_test.py
UNIT_TEST_RESULT=$?

# Check if all tests passed
if [ "$TEST_RESULT" != '0' ] || [ "$UNIT_TEST_RESULT" != '0' ]; then
    echo "❌ Tests failed!"
    dfx stop
    exit 1
else
    echo "✅ All tests passed successfully!"
fi

echo "Stopping dfx..."
dfx stop

echo "All done!"