#!/bin/bash
set -e
set -x

# Start dfx in the background
echo "Starting dfx..."
dfx start --background --clean > src/log.txt 2>&1

# Deploy the test canister
echo "Deploying test canister..."
dfx deploy

# Define a list of test identifiers
TEST_IDS=( )  # TODO: populate this list with test case ids

# Loop through each test identifier
for TEST_ID in "${TEST_IDS[@]}"; do
  echo "Testing test_${TEST_ID} module..."
  dfx canister call test run_test ${TEST_ID}
  sleep 2
  
  (cd src && PYTHONPATH=. python tests/test_functions.py assert ${TEST_ID})
  TEST_RESULT=$?
  
  if [ "$TEST_RESULT" != '0' ]; then
    echo "Error: test_${TEST_ID}.run() function returned unexpected result: $TEST_RESULT"
    dfx stop
    exit 1
  else
    echo "test_${TEST_ID}.run() function test passed!"
  fi

done

echo "Stopping dfx..."
dfx stop

echo "All done!"