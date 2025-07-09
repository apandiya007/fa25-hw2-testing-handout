"""
sorting.py
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.

BUGGY VERSION FOR HW2 - Students need to write tests to debug this code!
"""

import pandas as pd
import numpy as np
from typing import Dict, Union, Optional, List

class CaseSorter:
    """
    Class for sorting and ranking 311 cases.
    Contains intentional bugs for students to find and fix.
    """

    def __init__(self):
        """Initialize CaseSorter with default urgency rankings."""
        self._urgency_cache = {}  # Private cache for urgency rankings
        self.__default_urgency = 10  # Private default urgency score

    def sort_by_days_open(self, df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
        """
        Sort the 311 cases by how long they were open.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            ascending (bool): If True, sort from shortest to longest duration
            
        Returns:
            pd.DataFrame: Sorted dataset
            
        Raises:
            KeyError: If 'days_open' column doesn't exist
            ValueError: If days_open contains non-numeric values
        """
        if 'days_open' not in df.columns:
            raise KeyError("Column 'days_open' not found in dataset")

        # BUG 1: Not handling non-numeric values properly
        # Should convert to numeric first and handle errors
        df_sorted = df.sort_values('days_open', ascending=ascending)

        # BUG 2: Modifying original dataframe instead of returning copy
        return df_sorted  # Should return df_sorted.copy()

    def create_urgency_ranking(self, df: pd.DataFrame) -> Dict[str, int]:
        """
        Create an urgency ranking system for 311 case categories.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            
        Returns:
            Dict[str, int]: Dictionary mapping categories to urgency scores 
                           (1 = most urgent, higher = less urgent)
            
        Raises:
            KeyError: If 'category' column doesn't exist
        """
        if 'category' not in df.columns:
            raise KeyError("Column 'category' not found in dataset")

        categories = df['category'].unique()
        print("Available categories in your dataset:")
        print("-" * 40)
        for i, cat in enumerate(sorted(categories), 1):
            print(f"{i:2d}. {cat}")

        print(f"\nTotal categories: {len(categories)}")

        # BUG 3: Hard-coded urgency ranking that may not match actual data categories
        urgency_ranking = {
            'Traffic Signal Repair': 1,
            'Street Defects': 2,
            'Blocked Bike Lane': 3,
            'Street and Sidewalk Cleaning': 4,
            'Pothole': 5,
            'Tree Maintenance': 6,
            'Graffiti Removal': 7,
            'Noise Complaint': 8,
            'Parking Violation': 9,
            'General Inquiry': 10
        }

        # BUG 4: Not handling categories that aren't in the ranking
        # Should assign default values or raise error
        return urgency_ranking

    def filter_data(self, df: pd.DataFrame, urgency_ranking: Dict[str, int]) -> pd.DataFrame:
        """
        Filter the dataset to include only the categories that have been ranked.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            urgency_ranking (Dict[str, int]): Urgency ranking dictionary
            
        Returns:
            pd.DataFrame: Filtered dataset
            
        Raises:
            ValueError: If urgency_ranking is empty
            KeyError: If 'category' column doesn't exist
        """
        if not urgency_ranking:
            raise ValueError("Urgency ranking dictionary is empty")

        if 'category' not in df.columns:
            raise KeyError("Column 'category' not found in dataset")

        return filtered_df

    def sort_by_urgency(self, df: pd.DataFrame, urgency_ranking: Dict[str, int]) -> pd.DataFrame:
        """
        Sort 311 cases by urgency ranking.
        
        Args:
            df (pd.DataFrame): The 311 cases dataset
            urgency_ranking (Dict[str, int]): Dictionary mapping categories to urgency scores
            
        Returns:
            pd.DataFrame: Dataset sorted by urgency (most urgent first)
            
        Raises:
            ValueError: If urgency_ranking is empty
            KeyError: If 'category' column doesn't exist
        """
        if not urgency_ranking:
            raise ValueError("Urgency ranking dictionary is empty")

        if 'category' not in df.columns:
            raise KeyError("Column 'category' not found in dataset")

        # BUG 6: Creating a copy but then modifying original
        df_copy = df.copy()

        # BUG 7: Wrong way to map urgency scores - should use .map() not direct assignment
        df['urgency_score'] = urgency_ranking[df['category']]  # This will cause KeyError

        # BUG 8: Wrong sort order - should sort by urgency_score first, then days_open
        sorted_df = df_copy.sort_values(['days_open', 'urgency_score'], 
                                       ascending=[False, True])

        return sorted_df

    def _calculate_priority_score(self, urgency: int, days_open: int) -> float:
        """
        Private method to calculate priority score.
        Should not be accessed externally.
        
        Args:
            urgency (int): Urgency ranking (1-10)
            days_open (int): Number of days case has been open
            
        Returns:
            float: Priority score
        """
        # BUG 9: Division by zero possibility and illogical formula
        return days_open / urgency  # Should handle urgency = 0


# Legacy functions for backward compatibility
def sort_by_days_open(df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    """
    Legacy function - Sort the 311 cases by how long they were open.
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        ascending (bool): If True, sort from shortest to longest duration
        
    Returns:
        pd.DataFrame: Sorted dataset
    """
    sorter = CaseSorter()
    return sorter.sort_by_days_open(df, ascending)


def create_urgency_ranking(df: pd.DataFrame) -> Dict[str, int]:
    """
    Legacy function - Create an urgency ranking system for 311 case categories.
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        
    Returns:
        Dict[str, int]: Dictionary mapping categories to urgency scores
    """
    sorter = CaseSorter()
    return sorter.create_urgency_ranking(df)


# BUG 10: Function with wrong parameter type hint
def filter_data(df: pd.DataFrame, urgency_ranking: str) -> pd.DataFrame:
    """
    Legacy function with WRONG type hint - should be Dict[str, int], not str.
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        urgency_ranking (str): Should be Dict[str, int] but incorrectly typed as str
        
    Returns:
        pd.DataFrame: Filtered dataset
    """
    sorter = CaseSorter()
    return sorter.filter_data(df, urgency_ranking)


def sort_by_urgency(df: pd.DataFrame, urgency_ranking: Dict[str, int]) -> pd.DataFrame:
    """
    Legacy function - Sort 311 cases by urgency ranking.
    
    Args:
        df (pd.DataFrame): The 311 cases dataset
        urgency_ranking (Dict[str, int]): Dictionary mapping categories to urgency scores
        
    Returns:
        pd.DataFrame: Dataset sorted by urgency (most urgent first)
    """
    sorter = CaseSorter()
    return sorter.sort_by_urgency(df, urgency_ranking)
