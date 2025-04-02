import sys
import os
import time

print("\n=====================================================")
print("🔍 STARTING CLI IMPORT TESTS at", time.strftime("%Y-%m-%d %H:%M:%S"))
print("=====================================================\n")

# Add the src directory to the Python path
src_path = os.path.abspath("/app/src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

print("Attempting to import kybra_simple_shell modules...")
print(f"Python path: {sys.path}")

try:
    # Import directly from the src directory
    print("Importing kybra_simple_shell module...")
    import kybra_simple_shell
    print("Importing cli module...")
    from kybra_simple_shell.cli import main
    print("Importing shell module...")
    from kybra_simple_shell.shell import KybraShell
    
    # Create a shell instance to verify the class is working
    shell = KybraShell(canister_name="test")
    
    print("\n✓ Successfully imported and instantiated KybraShell")
    print("✓ CLI tool is properly installed and importable")
    print(f"Module location: {kybra_simple_shell.__file__}")
    print("\n✅ ALL CLI IMPORT TESTS PASSED SUCCESSFULLY!")
    print("=====================================================\n")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print("\n❌ CLI IMPORT TESTS FAILED!")
    print("=====================================================\n")
    sys.exit(1)
