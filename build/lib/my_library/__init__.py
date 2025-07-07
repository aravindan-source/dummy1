# __init__.py: Makes the folder a package.
# core.py: Your main module with functions/classes.
# tests/: Unit tests for your library.
# setup.py and pyproject.toml: For packaging and distribution.
'''
my_library/
├── my_library/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_core.py
├── README.md
├── setup.py
└── pyproject.toml
'''
# __init__.py
from .core import greet
from .core import Person

# This file is intentionally left empty. It serves to mark the directory as a Python package.
# Now users can do: from my_library import greet
__all__ = ['greet', 'Person']  # Specify what should be imported when using 'from my_library import *'