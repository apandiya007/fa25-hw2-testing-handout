"""
sorting.py
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.

BUGGY VERSION FOR HW2 - Students need to write tests to debug this code!
"""
import pandas as pd

class CaseSorter:
    """
    Class for sorting and ranking 311 cases.
    Contains intentional bugs for students to find and fix.
    """

    def __init__(self) -> None:
        """Initialize CaseSorter with default urgency rankings."""
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass
