import subprocess
import sys
import re
import time

print("\n=====================================================")
print("🚀 STARTING SHELL COMMAND TESTS at", time.strftime("%Y-%m-%d %H:%M:%S"))
print("=====================================================\n")

# Commands to test
test_commands = [
    "print('Hello from Kybra Simple Shell')",
    "a = 42",
    "print(a)",
    "a * 2",
    "import sys",
    "print(sys.version)"
]

# Function to execute a shell command and return output
def run_command(cmd):
    try:
        # Create a command that sends the test input to the shell
        # Escape quotes properly for Candid format
        escaped_cmd = cmd.replace('"', '\\"').replace("'", "\\'") 
        dfx_cmd = [
            "dfx", 
            "canister", 
            "call", 
            "test", 
            "execute_code", 
            f'("{escaped_cmd}")'
        ]
        result = subprocess.run(dfx_cmd, capture_output=True, text=True, check=True)
        # Extract result from dfx output
        output = result.stdout.strip()
        # The output format may be wrapped in a tuple notation like ("result")
        match = re.search(r'\(\s*"(.*?)"\s*\)', output, re.DOTALL)
        if match:
            # Unescape special characters and handle multi-line output
            response = match.group(1).replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
            return response
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# Run tests
print("\n📋 Running test suite with", len(test_commands), "test commands...")
print("📋 Python version:", sys.version)
print("📋 Testing against canister ID: [Will be determined from dfx output]\n")
failed = False
for cmd in test_commands:
    print(f"\nExecuting: {cmd}")
    output = run_command(cmd)
    print(f"Output:\n{output}")
    
    # Validate results for specific commands
    if cmd == "print('Hello from Kybra Simple Shell')":
        if "Hello from Kybra Simple Shell" not in output:
            print("ERROR: Expected greeting not found in output")
            failed = True
        else:
            print("✓ Hello test passed")
    
    if cmd == "a = 42":
        # This is an assignment, should have no error
        if "Error" in output or "TypeError" in output or "SyntaxError" in output:
            print("ERROR: Variable assignment failed")
            failed = True
        else:
            print("✓ Assignment test passed")
    
    if cmd == "print(a)":
        if "42" not in output:
            print("ERROR: Variable a not set or returned correctly")
            failed = True
        else:
            print("✓ Variable access test passed")
    
    if cmd == "a * 2":
        if "84" not in output:
            print("ERROR: Expression evaluation failed")
            failed = True
        else:
            print("✓ Expression evaluation test passed")

# Summarize test results
if not failed:
    print("\n✅ ALL SHELL TESTS PASSED SUCCESSFULLY!")
    print("=====================================================\n")
else:
    print("\n❌ SOME SHELL TESTS FAILED!")
    print("=====================================================\n")
    
# Exit with appropriate status
sys.exit(1 if failed else 0)
