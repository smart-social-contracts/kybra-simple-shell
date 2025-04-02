import unittest
from unittest.mock import patch, MagicMock
import sys
import io
from kybra_simple_shell.cli import main

class TestCLI(unittest.TestCase):
    
    @patch('kybra_simple_shell.cli.KybraShell')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main_default_canister(self, mock_parse_args, mock_kybra_shell):
        """Test that main creates a KybraShell with default canister name."""
        # Mock the parsed arguments
        mock_args = MagicMock()
        mock_args.canister = "my_canister"
        mock_parse_args.return_value = mock_args
        
        # Mock KybraShell instance
        mock_shell_instance = MagicMock()
        mock_kybra_shell.return_value = mock_shell_instance
        
        # Call the main function
        main()
        
        # Verify KybraShell was created with the right canister name
        mock_kybra_shell.assert_called_once_with(canister_name="my_canister")
        
        # Verify run_shell was called
        mock_shell_instance.run_shell.assert_called_once()
    
    @patch('kybra_simple_shell.cli.KybraShell')
    def test_main_custom_canister(self, mock_kybra_shell):
        """Test that main creates a KybraShell with custom canister name."""
        # Mock the KybraShell instance
        mock_shell_instance = MagicMock()
        mock_kybra_shell.return_value = mock_shell_instance
        
        # Mock command line arguments
        test_args = ['--canister', 'custom_canister']
        with patch.object(sys, 'argv', ['kybra-simple-shell'] + test_args):
            main()
            
            # Verify KybraShell was created with the custom canister name
            mock_kybra_shell.assert_called_once_with(canister_name='custom_canister')
            
            # Verify run_shell was called
            mock_shell_instance.run_shell.assert_called_once()

if __name__ == '__main__':
    unittest.main()
