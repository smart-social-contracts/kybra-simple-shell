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
        mock_args.canister_id = "test_canister"
        mock_args.network = None
        mock_args.ic = False
        mock_parse_args.return_value = mock_args
        
        # Mock KybraShell instance
        mock_shell_instance = MagicMock()
        mock_kybra_shell.return_value = mock_shell_instance
        
        # Call the main function
        main()
        
        # Verify KybraShell was created with the right parameters
        mock_kybra_shell.assert_called_once_with(canister_name="test_canister", network=None)
        
        # Verify run_shell was called
        mock_shell_instance.run_shell.assert_called_once()
    
    @patch('kybra_simple_shell.cli.KybraShell')
    def test_main_with_network(self, mock_kybra_shell):
        """Test that main creates a KybraShell with network parameter."""
        # Mock the KybraShell instance
        mock_shell_instance = MagicMock()
        mock_kybra_shell.return_value = mock_shell_instance
        
        # Mock command line arguments
        test_args = ['custom_canister', '--network', 'local']
        with patch.object(sys, 'argv', ['kybra-simple-shell'] + test_args):
            main()
            
            # Verify KybraShell was created with the right parameters
            mock_kybra_shell.assert_called_once_with(canister_name='custom_canister', network='local')
            
            # Verify run_shell was called
            mock_shell_instance.run_shell.assert_called_once()

if __name__ == '__main__':
    unittest.main()
