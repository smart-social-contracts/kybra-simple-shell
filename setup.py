from setuptools import setup, find_packages

setup(
    name="kybra-simple-shell",
    version="0.1.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kybra-simple-shell=kybra_simple_shell.cli:main",
        ],
    },
    install_requires=["prompt_toolkit>=3.0.0"],
    description="A lightweight CLI tool for interacting with Python-based Kybra canisters",
    author="Kybra Team",
    url="https://github.com/your-org/kybra-simple-shell",
)
