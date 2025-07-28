"""
data_loader.py
Module responsible for loading and basic exploration of 311 cases dataset.
Follows single responsibility principle: handles data input and initial exploration.

BUGGY VERSION FOR HW2 - Students need to write tests to debug this code!
"""
import pandas as pd

class DataLoader:
    """
    Class for loading and managing 311 cases data.
    Contains intentional bugs for students to find and fix.
    """

    def __init__(self, filepath: str):
        """
        Initialize DataLoader with file path.
        
        Args:
            filepath (str): Path to the CSV file
        """
        pass

    def load_and_explore_data(self) -> pd.DataFrame:
        """
        Load the 311 cases dataset and display basic information.
        
        Returns:
            pd.DataFrame: Loaded dataset
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If data cannot be loaded
        """
        pass

    def _validate_required_columns(self) -> bool:
        """
        Private method to validate that required columns exist.
        Should only be called internally.
        
        Returns:
            bool: True if all required columns exist
            
        Raises:
            KeyError: If required columns are missing
        """
        pass


    def get_basic_stats(self) -> dict[str, any]:
        """
        Get basic statistics about the loaded dataset.
        
        Returns:
            Dict[str, Any]: Dictionary containing basic statistics
            
        Raises:
            ValueError: If data hasn't been loaded yet
        """
        return None
        pass

    def filter_by_city(self, cities: list[str]) -> pd.DataFrame:
        """
        Filter data by city names (Oakland vs Boston).
        
        Args:
            cities (List[str]): List of city names to filter by
            
        Returns:
            pd.DataFrame: Filtered dataset
            
        Raises:
            TypeError: If cities is not a list
            ValueError: If no data matches the filter
        """
        pass

    @property
    def is_processed(self) -> bool:
        """
        Check if data has been processed.
        
        Returns:
            bool: True if data is processed
        """
        pass

    def _get_raw_data(self) -> pd.DataFrame:
        """
        Private method to get raw data - should not be called externally.
        
        Returns:
            pd.DataFrame: Raw dataset
        """
        pass
