#!/bin/bash
set -e
set -x

IMAGE_ADDRESS="ghcr.io/smart-social-contracts/icp-dev-env:latest"

echo "Running tests..."
docker run --rm \
    -v "${PWD}/src:/app/src" \
    -v "${PWD}/../kybra_simple_shell:/app/src/kybra_simple_shell" \
    -v "${PWD}/dfx.json:/app/dfx.json" \
    -v "${PWD}/entrypoint.sh:/app/entrypoint.sh" \
    -v "${PWD}/test_shell_commands.py:/app/test_shell_commands.py" \
    -v "${PWD}/cli_test.py:/app/cli_test.py" \
    --entrypoint "/app/entrypoint.sh" \
    $IMAGE_ADDRESS || {
    echo "❌ Tests failed"
    exit 1
}

echo "✅ All tests passed successfully!"