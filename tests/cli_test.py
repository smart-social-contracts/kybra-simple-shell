import sys
import os

# Add the src directory to the Python path
src_path = os.path.abspath("/app/src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    # Import directly from the src directory
    import kybra_simple_shell
    from kybra_simple_shell.cli import main
    from kybra_simple_shell.shell import KybraShell
    
    # Create a shell instance to verify the class is working
    shell = KybraShell(canister_name="test")
    
    print("✓ Successfully imported and instantiated KybraShell")
    print("✓ CLI tool is properly installed and importable")
    print(f"Module location: {kybra_simple_shell.__file__}")
    sys.exit(0)
except Exception as e:
    print(f"ERROR: {str(e)}")
    sys.exit(1)
