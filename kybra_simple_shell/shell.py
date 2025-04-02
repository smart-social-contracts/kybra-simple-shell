import subprocess
import json
import re
import sys
import platform
import pkg_resources
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

class KybraShell:
    def __init__(self, canister_name="my_canister", network=None):
        self.canister_name = canister_name
        self.network = network
        self.globals_dict = {}
    
    def execute(self, code):
        """
        Sends Python code to the canister's exec method and returns the result.
        """
        # Escape double quotes in the code
        escaped_code = code.replace('"', '\\"')
        
        # Prepare the dfx command
        cmd = [
            "dfx", 
            "canister", 
            "call"
        ]
        
        # Add network parameter if provided
        if self.network:
            cmd.extend(["--network", self.network])
            
        # Add the rest of the command
        cmd.extend([
            self.canister_name, 
            "execute_code", 
            f'("{escaped_code}")'
        ])
        
        try:
            # Execute the dfx command
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Parse the output
            output = result.stdout.strip()
            
            # Extract the actual response from dfx output format
            # The output is typically in the format: (result)
            match = re.search(r'\("(.*)"\)', output)
            if match:
                # The canister returns a string that may contain escaped characters
                response = match.group(1)
                # Unescape any escaped characters
                response = response.replace('\\n', '\n').replace('\\"', '"')
                return response
            
            return output
        except subprocess.CalledProcessError as e:
            return f"Error calling canister: {e.stderr}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_dfx_version(self):
        """
        Get the installed dfx version
        """
        try:
            result = subprocess.run(["dfx", "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            return "dfx not found or error getting version"
        except Exception:
            return "dfx not found or error getting version"
    
    def get_kybra_version(self):
        """
        Get the installed Kybra version
        """
        try:
            kybra_version = pkg_resources.get_distribution("kybra").version
            return kybra_version
        except Exception:
            return "Kybra not found or error getting version"
            
    def show_help(self):
        """
        Show help information
        """
        print("\nKybra Simple Shell Help:")
        print("  :q           - Quit the shell")
        print("  :help        - Show this help message")
        print("\nNavigation:")
        print("  Up Arrow     - Go to previous command in history")
        print("  Down Arrow   - Go to next command in history")
        print("\nYou can execute Python code directly in this shell.")
        print("The code will be sent to your Kybra canister for execution.")
        print("Example: print('Hello from canister!')")
        print()
    
    def run_shell(self):
        """
        Runs an interactive shell for executing Python code on the canister.
        """
        # Get version information
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        python_implementation = platform.python_implementation()
        dfx_version = self.get_dfx_version()
        kybra_version = self.get_kybra_version()
        
        # Display welcome message with version info
        print(f"Kybra Simple Shell v{pkg_resources.get_distribution('kybra-simple-shell').version}")
        print(f"Python {python_version} ({python_implementation}) on {platform.system()}")
        print(f"DFX: {dfx_version}")
        print(f"Kybra: {kybra_version}")
        print(f"Canister: {self.canister_name}")
        print(f"Network: {self.network if self.network else 'local'}")
        print("Type ':q' to quit, ':help' for help")
        print("Arrow keys ↑↓ can be used to navigate command history")
        print()
        
        # Create a prompt session with history
        history = InMemoryHistory()
        session = PromptSession(history=history)
        
        while True:
            try:
                # Get user input with prompt_toolkit (supports arrow key navigation)
                user_input = session.prompt(">>> ")
                
                # Check for shell commands
                if user_input.strip() == ":q":
                    break
                elif user_input.strip() == ":help":
                    self.show_help()
                
                # If not a shell command, send to canister
                if user_input.strip():
                    result = self.execute(user_input)
                    if result:
                        print(result, end="")
            
            except KeyboardInterrupt:
                print("\nUse ':q' to quit")
            except EOFError:
                break
            except Exception as e:
                print(f"Shell error: {str(e)}")
        
        print("Goodbye!")
