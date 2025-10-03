"""
sorting.py
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.

BUGGY VERSION FOR HW2 - Students need to write tests to debug this code!
"""

import pandas as pd
import numpy as np

class CaseSorter:
    """
    Class for sorting and ranking 311 cases.
    Contains intentional bugs for students to find and fix.
    """

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
        if "days_open" not in df.columns:
            raise KeyError("Missing required column: days_open")
        
        # ensures numerics
        if not pd.api.types.is_numeric_dtype(df["days_open"]):
            raise ValueError("Column 'days_open' must contain numeric values")
        
        return df.sort_values(by="days_open", ascending=ascending, ignore_index=True)


    def create_urgency_ranking(self, df: pd.DataFrame) -> dict[str, int]:
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
        if "category" not in df.columns:
            raise KeyError("Missing required column: category")
        
        categories = df["category"].dropna().unique()

        # Assigns urgency based on order of appearance
        ranking = {cat: rank + 1 for rank, cat in enumerate(categories)}

        if not ranking:
            raise ValueError("Urgency ranking could not be created (no categories found)")
        
        return ranking

    def filter_data(self, df: pd.DataFrame, urgency_ranking: dict[str, int]) -> pd.DataFrame:
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
            raise ValueError("Urgency ranking is empty")
        
        if "category" not in df.columns:
            raise KeyError("Missing required column: category")
        
        filtered = df[df["category"].isin(urgency_ranking.keys())]

        if filtered.empty:
            raise ValueError("No data matches the urgency ranking")
        
        return filtered.reset_index(drop=True)


    def sort_by_urgency(self, df: pd.DataFrame, urgency_ranking: dict[str, int]) -> pd.DataFrame:
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
            raise ValueError("Urgency ranking is empty")
        
        if "category" not in df.columns:
            raise KeyError("Missing required column: category")
        
        if "days_open" not in df.columns:
            raise KeyError("Missing required column: days_open")
        
        #checks for numeric days_open
        if not pd.api.types.is_numeric_dtype(df["days_open"]):
            raise ValueError("Column 'days_open' must contain numeric values")
        
        missing = set(df["category"].unique()) - set(urgency_ranking.keys())
        if missing:
            raise ValueError(f"Urgency ranking missing categories: {missing}")
        
        df = df.copy()
        df["urgency_score"] = df["category"].map(urgency_ranking)

        return df.sort_values(
            by=["urgency_score", "days_open"],
            ascending=[True, False], 
            ignore_index=True
        )


        


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
        if not isinstance(urgency, (int, np.integer)) or not isinstance(days_open, (int, np.integer)):
            raise ValueError("Urgency and days_open must be integers")
        
        #Lower urgency is more important
        return 1 / urgency + (days_open / 100.0)
