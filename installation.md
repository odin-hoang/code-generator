# Installation Guide

This guide will help you set up and install the Code Generator Odin on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher
- `pip` (Python package installer)
- `git` (version control system)

## Steps

### 1. Clone the Repository

First, clone the repository from GitHub:

```sh
git clone https://github.com/odin-hoang/code-generator.git
cd code-generator
```

### 2. Install Dependencies

Install the required dependencies using `pip`:

```sh
pip install .
```

For development, you can install the package with testing dependencies:

```sh
pip install -e .[test]
```

### 3. Verify installation

To verify that the installation was successful, you can run the following command to display the help message:

```sh
generate-code -v
```

You should see the version number of the Code Generator Odin.

## Uninstallation

To uninstall the Code Generator Odin, simply run:

```sh
pip uninstall code-generator
```

If you encounter any issues during installation, please check the following:

- Ensure that Python and `pip` are correctly installed and added to your system's PATH.
- Ensure that you have the necessary permissions to install packages.
  For further assistance, please open an issue on the [GitHub repository](https://github.com/odin-hoang/code-generator/issues).
