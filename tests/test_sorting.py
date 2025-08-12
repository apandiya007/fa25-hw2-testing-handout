"""
test_sorting.py
Test file for sorting.py module.

Instructions for students:
1. Read the sorting.py module to understand its functionality.
2. Write comprehensive unit tests for all functions and methods in sorting.py.
3. Ensure to cover edge cases and exception handling as documented.
"""

import unittest
from src.sorting import CaseSorter

class TestCaseSorter (unittest.TestCase):
    """Test cases for CaseSorter class."""
    # Write tests for CaseSorter class, covering all methods and exceptions that are documented.

    def setUp(self) -> None:
        """Set up CaseSorter instance for testing."""
        self.sorter = CaseSorter()
