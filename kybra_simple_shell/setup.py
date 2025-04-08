from setuptools import find_packages, setup

setup(
    name="kybra-simple-shell",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kybra-simple-shell=kybra_simple_shell.cli:main",
        ],
    },
    install_requires=[],
    description="A lightweight CLI tool for interacting with Python-based Kybra canisters",
    author="Smart Social Contracts Team",
    url="https://github.com/smart-social-contracts/kybra-simple-shell",
)
