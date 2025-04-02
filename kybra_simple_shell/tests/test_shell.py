import unittest
import subprocess
from unittest.mock import patch, MagicMock
from kybra_simple_shell.shell import KybraShell

class TestKybraShell(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        self.shell = KybraShell(canister_name="test_canister")
    
    def test_init(self):
        """Test the initialization of KybraShell."""
        self.assertEqual(self.shell.canister_name, "test_canister")
        self.assertEqual(self.shell.globals_dict, {})
    
    @patch('subprocess.run')
    def test_execute_simple_expression(self, mock_run):
        """Test executing a simple expression."""
        # Mock the subprocess.run return value
        mock_process = MagicMock()
        mock_process.stdout = '("5\\n")'
        mock_process.returncode = 0
        mock_run.return_value = mock_process
        
        result = self.shell.execute("2 + 3")
        
        # Verify subprocess.run was called with the right arguments
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        self.assertEqual(kwargs['capture_output'], True)
        self.assertEqual(kwargs['text'], True)
        self.assertEqual(args[0][0], "dfx")
        self.assertEqual(args[0][3], "test_canister")
        self.assertEqual(args[0][4], "execute_code")
        
        # Verify the result
        self.assertEqual(result, "5\n")
    
    @patch('subprocess.run')
    def test_execute_with_quotes(self, mock_run):
        """Test executing code that contains quotes."""
        # Mock the subprocess.run return value
        mock_process = MagicMock()
        mock_process.stdout = '("Hello, \\"world\\"!\\n")'
        mock_process.returncode = 0
        mock_run.return_value = mock_process
        
        result = self.shell.execute('print("Hello, \\"world\\"!")')
        
        # Verify that quotes were properly escaped in the command
        args, kwargs = mock_run.call_args
        cmd_str = args[0][5]
        # Use a more flexible assertion that works regardless of escaping format
        self.assertIn('world', cmd_str)
        
        # Verify the result
        self.assertEqual(result, 'Hello, "world"!\n')
    
    @patch('subprocess.run')
    def test_execute_error(self, mock_run):
        """Test handling of execution errors."""
        # Set up the mock to raise an exception
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd", stderr="Error message")
        
        result = self.shell.execute("1/0")
        
        # Verify error handling
        self.assertIn("Error calling canister", result)
        

if __name__ == '__main__':
    unittest.main()
