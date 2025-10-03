"""
test_sorting.py
Test file for sorting.py module.

Instructions for students:
1. Read the sorting.py module to understand its functionality.
2. Write comprehensive unit tests for all functions and methods in sorting.py.
3. Ensure to cover edge cases and exception handling as documented.
"""

import unittest
import pandas as pd
import numpy as np
from src.sorting import CaseSorter

class TestCaseSorter (unittest.TestCase):
    """Test cases for CaseSorter class."""
    # Write tests for CaseSorter class, covering all methods and exceptions that are documented.

    def setUp(self) -> None:
        """Set up CaseSorter instance for testing."""
        self.sorter = CaseSorter()

        self.df = pd.DataFrame({
            "category": ["Graffiti", "Encampments", "Street Cleaning", "Graffiti"],
            "days_open": [10, 200, 5, 100],
        })
    
    def test_sort_by_days_open_descending(self) -> None:
        sorted_df = self.sorter.sort_by_days_open(self.df, ascending=False)
        self.assertEqual(sorted_df.iloc[0]["days_open"], 200) 
    
    def test_sort_by_days_open_ascending(self) -> None:
        sorted_df = self.sorter.sort_by_days_open(self.df, ascending=True)
        self.assertEqual(sorted_df.iloc[0]["days_open"], 5) 
    
    def test_sort_by_days_open_missing_column(self) -> None:
        df = pd.DataFrame({"category": ["Graffiti"]})
        with self.assertRaises(KeyError):
            self.sorter.sort_by_days_open(df)
    
    def test_sort_by_days_open_non_numeric(self) -> None:
        df = pd.DataFrame({"category": ["Graffiti"], "days_open": ["ten"]})
        with self.assertRaises(KeyError):
            self.sorter.sort_by_days_open(df)
    
    def test_create_urgency_ranking_success(self) -> None:
        ranking = self.sorter.create_urgency_ranking(self.df)
        self.assertIn("Graffiti", ranking)
        self.assertIsInstance(ranking["Graffiti"], int)
    
    def test_create_urgency_ranking_missing_column(self) -> None:
        df = pd.DataFrame({"days_open": [1, 2, 3]})
        with self.assertRaises(KeyError):
            self.sorter.create_urgency_ranking(df)
    
    def test_create_urgency_ranking_empty(self) -> None:
        df = pd.DataFrame({"category": []})
        with self.assertRaises(ValueError):
            self.sorter.create_urgency_ranking(df)
    
    def test_filter_data_success(self) -> None:
        ranking = {"Graffiti": 1, "Encampments": 2}
        filtered = self.sorter.filter_data(self.df, ranking)
        self.assertTrue(all(filtered["category"].isin(ranking.keys())))

    def test_filter_data_empty_ranking(self) -> None:
        with self.assertRaises(ValueError):
             self.sorter.filter_data(self.df, {})
    
    def test_filter_data_missing_column(self) -> None:
        df = pd.DataFrame({"days_open": [1, 2]})
        with self.assertRaises(KeyError):
            self.sorter.filter_data(df, {"Graffiti": 1})
    
    def test_filter_data_no_matches(self) -> None:
        ranking = {"Nonexistent": 1}
        with self.assertRaises(ValueError):
            self.sorter.filter_data(self.df, ranking)
    
    def test_sort_by_urgency_success(self) -> None:
        ranking = {"Graffiti": 1, "Encampments": 2, "Street Cleaning": 3}
        sorted_df = self.sorter.sort_by_urgency(self.df, ranking)
        self.assertEqual(sorted_df.iloc[0]["category"], "Graffiti")
    
    def test_sort_by_urgency_empty_ranking(self) -> None:
        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency(self.df, {})
    
    def test_sort_by_urgency_missing_category_column(self) -> None:
        df = pd.DataFrame({"days_open": [1, 2, 3]})
        with self.assertRaises(KeyError):
            self.sorter.sort_by_urgency(df, {"Graffiti": 1})
    
    def test_sort_by_urgency_missing_days_open(self) -> None:
        df = pd.DataFrame({"category": ["Graffiti"]})
        with self.assertRaises(KeyError):
            self.sorter.sort_by_urgency(df, {"Graffiti": 1})
    
    def test_sort_by_urgency_non_numeric_days_open(self) -> None:
        df = pd.DataFrame({"category": ["Graffiti"],  "days_open": ["NaN"]})
        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency(df, {"Graffiti": 1})
    
    def test_sort_by_urgency_missing_categories_in_ranking(self) -> None:
        ranking = {"Graffiti": 1}
        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency(self.df, ranking)
    
    def test_calculate_priority_score_success(self) -> None:
        score = self.sorter._calculate_priority_score(urgency=1, days_open=100)
        self.assertIsInstance(score, float)
    
    def test_calculate_priority_score_invalid_types(self) -> None:
        with self.assertRaises(ValueError):
            self.sorter._calculate_priority_score("high", 10)
    
if __name__ == "__main__":
    unittest.main()
      

    











    

    

    

    



