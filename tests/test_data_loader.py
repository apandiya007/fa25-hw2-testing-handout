"""
test_data_loader.py
Test file for data_loader.py module.

Instructions for students:
1. Run these tests to see which ones fail
2. Identify the bugs in data_loader.py based on the test failures
3. Fix the bugs in data_loader.py until all tests pass
4. Add additional tests as needed to improve coverage

Run with: pytest test_data_loader.py -v
"""

import pytest
import pandas as pd
import numpy as np
import tempfile
import os
from src.data_loader import DataLoader, load_and_explore_data


class TestDataLoader:
    """Test cases for DataLoader class."""

    def test_init(self):
        """Test DataLoader initialization."""
        # Write test for DataLoader initialization
        # Check filepath, _data, and is_processed attributes
        pass

    def test_load_and_explore_data_success(self, csv):
        """Test successful data loading."""
        # Write test to load valid CSV file
        # Check if data loads correctly and has expected shape/columns
        pass

    def test_load_nonexistent_file(self):
        """Test loading non-existent file."""
        # Write test for loading non-existent file
        # Should raise ValueError with appropriate message
        pass

    def test_validate_required_columns_missing(self, csv):
        """Test column validation with missing required columns."""
        # Write test for missing required columns
        # Should raise KeyError about missing columns
        pass

    def test_get_basic_stats_without_loading(self):
        """Test getting stats before loading data."""
        # Write test for getting stats before loading
        # Should raise ValueError
        pass

    def test_get_basic_stats_success(self, csv):
        """Test getting basic stats after loading data."""
        # Write test for successful stats retrieval
        # Check if stats contain expected keys and values
        pass

    def test_filter_by_city_list_input(self, csv):
        """Test filtering by city with list input."""
        # Write test for filtering with list of cities
        # Should return filtered dataframe
        pass

    def test_filter_by_city_string_input(self, csv):
        """Test filtering by city with string input."""
        # Write test for filtering with single city as string
        # Should handle string input gracefully
        pass

    def test_filter_by_city_case_insensitive(self, csv):
        """Test filtering by city with different case."""
        # Write test for case-insensitive filtering
        # Should work regardless of case
        pass

    def test_filter_by_city_no_matches(self, csv):
        """Test filtering by city with no matches."""
        # Write test for no matching cities
        # Should raise ValueError
        pass

    def test_filter_by_city_without_loading(self):
        """Test filtering before loading data."""
        # Write test for filtering before loading
        # Should raise ValueError
        pass

    def test_filter_by_city_type_error(self, csv):
        """Test filtering with wrong input type."""
        # Write test for wrong input type
        # Should raise TypeError for invalid types
        pass

    def test_is_processed_property(self, csv):
        """Test the is_processed property."""
        # Write test for is_processed property
        # Should be False initially, True after loading
        pass

    def test_legacy_function(self, csv):
        """Test the legacy load_and_explore_data function."""
        # Write test for legacy function
        # Should work the same as class method
        pass


class TestDataLoaderEdgeCases:
    """Additional edge case tests for DataLoader."""

    def test_empty_csv_file(self):
        """Test loading empty CSV file."""
        # Write test for empty CSV file
        # Should handle gracefully
        pass

    def test_csv_with_only_headers(self):
        """Test CSV file with only headers, no data."""
        # Write test for CSV with only headers
        # Should load but have 0 rows
        pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
