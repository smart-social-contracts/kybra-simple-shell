import unittest
import os
import sys

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.getcwd()))

# Import test modules directly since we're in the package directory
from tests import test_shell, test_cli

if __name__ == '__main__':
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromModule(test_shell))
    suite.addTests(loader.loadTestsFromModule(test_cli))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return appropriate exit code
    sys.exit(not result.wasSuccessful())
