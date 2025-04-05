# Kybra Simple Shell

A lightweight CLI tool for interacting with Python-based Kybra canisters on the Internet Computer (ICP). This acts as a remote REPL, letting you send Python code to your canister and see the output — including `stdout`, return values, and errors — right in your terminal.

---

## ✨ Features

- ✅ Seamless remote Python REPL over `dfx canister call`
- ✅ Captures `stdout`, `stderr`, and return values
- ✅ Simple commands (`:q` to quit, more coming)
- ✅ Packaged as a Python CLI: `kybra-simple-shell`

---

## 📦 Installation

First, clone the repo and install locally:

```bash
git clone https://github.com/your-org/kybra-simple-shell.git
cd kybra-simple-shell
pip install -e .
```

---

## ⚡ Quick Start with Example Canister

Want to try it out quickly? The repository includes a test canister with the required `execute_code` method:

```bash
# Clone the repository
git clone https://github.com/your-org/kybra-simple-shell.git
cd kybra-simple-shell

# Install the package
pip install -e .

# Navigate to the tests directory
cd tests

# Start a local Internet Computer replica
dfx start --clean --background

# Deploy the test canister
dfx deploy

# Use the shell with the test canister directly by name
kybra-simple-shell test
```

Now you can try Python commands in the shell:

```
>>> print("Hello from your canister!")
Hello from your canister!
>>> a = 42
>>> a * 2
84
>>> import math
>>> math.sqrt(16)
4.0

# You can access and interact with objects in the canister's memory
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.append(6)
>>> my_list
[1, 2, 3, 4, 5, 6]

# Objects persist between commands as they're stored in the canister's memory
>>> len(my_list)
6

# You can even import modules defined in your canister
>>> from tests import test_functions
>>> dir(test_functions)
```

When you're done, stop the local replica:

```bash
dfx stop
```

---

## 🚀 Usage
Before using the shell, make sure:

Your Kybra canister is running and deployed.

The canister has an exec(code: str) -> str update method that executes Python code remotely.

Start the shell
bash
Copy
Edit
kybra-simple-shell
Example interaction:
python-repl
Copy
Edit
Kybra Simple Shell (type ':q' to quit)

>>> a = 5
>>> print(a)
5
>>> a * 2
10
>>> 1 / 0
Traceback (most recent call last):
  File "<remote>", line 1, in <module>
ZeroDivisionError: division by zero
>>> :q
⚙️ Configuration
By default, the tool looks for a canister called my_canister.

You can edit shell.py to change the CANISTER_NAME, or add config file support (e.g., .kybra_shell.toml) as a future improvement.

🧠 How It Works
Under the hood, kybra-simple-shell wraps calls to:

bash
Copy
Edit
dfx canister call my_canister exec '(record { code = "..." })'
The canister executes the Python code, captures output and errors using io.StringIO, and returns everything as a string. The CLI parses and prints the result.

📚 Canister Requirements
Your Kybra canister should include this exec() method:

python
Copy
Edit
@update
def exec(code: str) -> str:
    import sys, io, traceback
    stdout = io.StringIO()
    stderr = io.StringIO()
    sys.stdout = stdout
    sys.stderr = stderr

    try:
        result = eval(code, globals())
        if result is not None:
            print(repr(result))
    except SyntaxError:
        try:
            exec(code, globals())
        except Exception:
            traceback.print_exc()
    except Exception:
        traceback.print_exc()

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    return stdout.getvalue() + stderr.getvalue()
📌 Future Plans
Multi-line input

Command history

Custom shell commands like :logs, :clear, :canister

Configurable canister name from .kybra_shell.toml
