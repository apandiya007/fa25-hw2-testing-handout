"""
test_data_loader.py
Test file for data_loader.py module.

Instructions for students:
1. Read the data_loader.py module to understand its functionality.
2. Complete all the test stubs provided below.
"""

import unittest
import pandas as pd
from src.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    """Test cases for DataLoader class."""

    def test_init(self) -> None:
        """Test DataLoader initialization."""
        # Write tests for DataLoader initialization
        # Check correct values of filepath and is_processed properties
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        self.assertEqual(loader.filepath, "example_CSVs/311_Cases_SF_Sample.csv")
        self.assertFalse(loader.is_processed)


    def test_load_and_explore_data_success(self) -> None:
        """Test successful data loading."""
        # Write test to load valid CSV file
        # Check if data loads correctly. This test has been written for you.
        # You may use this as a template for your other tests that involve checking
        # equality of a pandas DataFrame.
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        loaded_data = loader.load_and_explore_data()
        self.assertIsInstance(loaded_data, pd.DataFrame)
        self.assertTrue(loader.is_processed)
        self.assertIn("Neighborhood", loaded_data.columns)
        

        


    def test_load_nonexistent_file(self) -> None:
        """Test loading non-existent file."""
        # Write test for loading non-existent file
        loader = DataLoader("example_CSVs/does_not_exist.csv")
        with self.assertRaises(FileNotFoundError):
            loader.load_and_explore_data()

    def test_load_bad_file_format(self) -> None:
        """Test loading file with bad format."""
        # Write test for loading file with bad format,
        # using the provided bad_file_format.zip file.
        loader = DataLoader("example_CSVs/bad_file_format.zip")
        with self.assertRaises(ValueError):
            loader.load_and_explore_data()

    def test_validate_required_columns_missing(self) -> None:
        """Test column validation with missing required columns."""
        # Write test for loading a csv with missing required columns,
        # using the provided 311_Cases_missing_CaseID.csv file.
        loader = DataLoader("example_CSVs/311_Cases_missing_CaseID.csv")
        with self.assertRaises(KeyError):
            loader.load_and_explore_data()

    def test_get_basic_stats_without_loading(self) -> None:
        """Test getting stats before loading data."""
        # Write test for trying to get basic stats before loading data
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        with self.assertRaises(ValueError):
            loader.get_basic_stats()

    def test_get_basic_stats_success(self) -> None:
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        df = loader.load_and_explore_data()
        stats = loader.get_basic_stats()

        self.assertIsInstance(stats, dict)
        self.assertIn("shape", stats)
        self.assertIn("unique_neighborhoods", stats)

        self.assertEqual(stats["shape"], df.shape)
        self.assertEqual(stats["unique_neighborhoods"], df["Neighborhood"].nunique())




        



    def test_filter_by_neighborhood_list_input(self) -> None:
        """Test filtering by city with list input."""
        # Write test for filtering with list of neighborhoods
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        df = loader.load_and_explore_data()
        filtered = loader.filter_by_neighborhood(["Mission"])
        self.assertFalse(filtered.empty)
        self.assertTrue(all(filtered["Neighborhood"].str.lower() == "mission"))


    def test_filter_by_neighborhood_case_insensitive(self) -> None:
        """Test filtering by city with different case."""
        # Write test for case-insensitive filtering
        # Should work regardless of case
        # Write test for filtering with list of neighborhoods
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        df = loader.load_and_explore_data()
        filtered1 = loader.filter_by_neighborhood(["mission"])
        filtered2 = loader.filter_by_neighborhood(["MISSION"])
        self.assertTrue(filtered1.equals(filtered2))

    def test_filter_by_neighborhood_no_matches(self) -> None:
        """Test filtering by neighborhood with no matches."""
        # Write test for no matching cities
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        df = loader.load_and_explore_data()
        with self.assertRaises(ValueError):
            loader.filter_by_neighborhood(["Nonexistent Neighborhood"])

    def test_filter_by_neighborhood_without_loading(self) -> None:
        """Test filtering before loading data."""
        # Write test for filtering before loading
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        with self.assertRaises(ValueError):
            loader.filter_by_neighborhood(["Mission"])

if __name__ == "__main__":
    unittest.main()
