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


🚀 Usage
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
