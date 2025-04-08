# Kybra Simple Shell

A lightweight CLI tool for interacting with Python-based Kybra canisters on the Internet Computer (ICP). This acts as a remote REPL, letting you send Python code to your canister and see the output — including `stdout`, return values, and errors — right in your terminal.

[![Test](https://github.com/smart-social-contracts/kybra-simple-shell/actions/workflows/test.yml/badge.svg)](https://github.com/smart-social-contracts/kybra-simple-shell/actions)
[![PyPI version](https://badge.fury.io/py/kybra-simple-shell.svg)](https://badge.fury.io/py/kybra-simple-shell)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3107/)
[![License](https://img.shields.io/github/license/smart-social-contracts/kybra-simple-shell.svg)](https://github.com/smart-social-contracts/kybra-simple-shell/blob/main/LICENSE)

---

## ✨ Features

- ✅ Seamless remote Python REPL over `dfx canister call`
- ✅ Captures `stdout`, `stderr`, and return values
- ✅ Simple commands (`:q` to quit, `:help` for guidance)
- ✅ Packaged as a Python CLI: `kybra-simple-shell`
- ✅ Network selection support (local, IC mainnet via `--ic`, and custom networks)

---

## 📦 Installation

```bash
pip install kybra-simple-shell
```

---

## ⚡ Quick usage within your canister

```bash
# Recommended setup
pyenv install 3.10.7
pyenv local 3.10.7
python -m venv venv
source venv/bin/activate

# Install the package
pip install kybra-simple-shell
```

Now add the following code to your canister:

```python
from kybra import update, ic

@update
def execute_code(code: str) -> str:
    """Executes Python code and returns the output.

    This is the core function needed for the Kybra Simple Shell to work.
    It captures stdout, stderr, and return values from the executed code.
    """
    import io
    import sys
    import traceback

    stdout = io.StringIO()
    stderr = io.StringIO()
    sys.stdout = stdout
    sys.stderr = stderr

    try:
        # Try to evaluate as an expression
        result = eval(code, globals())
        if result is not None:
            ic.print(repr(result))
    except SyntaxError:
        try:
            # If it's not an expression, execute it as a statement
            # Use the built-in exec function but with a different name to avoid conflict
            exec_builtin = exec
            exec_builtin(code, globals())
        except Exception:
            traceback.print_exc()
    except Exception:
        traceback.print_exc()

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    return stdout.getvalue() + stderr.getvalue()

```

```bash
# Start a local Internet Computer replica
dfx start --clean --background

# Deploy the test canister
dfx deploy

# Use the shell with the test canister directly by name
kybra-simple-shell <MY_CANISTER_ID>              # Local network (default)
# kybra-simple-shell --ic <MY_CANISTER_ID>       # IC mainnet
```

```
>>> print("Hello from your canister!")
Hello from your canister!
>>> import my_library_inside_the_canister
>>> a = 42
>>>:q
Goodbye!
```

Now, connect to canister again and see any changes in memory:

```bash
kybra-simple-shell <MY_CANISTER_ID>
```

```
>>> print(a)
42
```

## 🔍 CLI Features

The shell provides helpful version information on startup (Python, DFX, Kybra versions) and supports commands like `:help` for guidance and `:q` to exit.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT