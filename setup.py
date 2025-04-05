from setuptools import setup, find_packages
import pathlib

# Read the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="kybra-simple-shell",
    version="0.1.3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kybra-simple-shell=kybra_simple_shell.cli:main",
        ],
    },
    install_requires=["prompt_toolkit>=3.0.0"],
    description="A lightweight CLI tool for interacting with Python-based Kybra canisters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kybra Team",
    url="https://github.com/your-org/kybra-simple-shell",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
