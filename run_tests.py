#!/usr/bin/env python3
import unittest
import sys
import os

# Add the parent directory to the path so we can import our package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Import the tests
from kybra_simple_shell.tests.test_shell import TestKybraShell
from kybra_simple_shell.tests.test_cli import TestCLI

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()
    
    # Add the test cases
    test_suite.addTest(unittest.makeSuite(TestKybraShell))
    test_suite.addTest(unittest.makeSuite(TestCLI))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Return appropriate exit code
    sys.exit(not result.wasSuccessful())
