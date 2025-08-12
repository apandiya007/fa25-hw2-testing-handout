"""
data_loader.py
Module responsible for loading and basic exploration of 311 cases dataset.
Follows single responsibility principle: handles data input and initial exploration.
"""
from typing import Any
import pandas as pd

class DataLoader:
    """
    Class for loading and managing 311 cases data.
    """

    def __init__(self, filepath: str):
        """
        Initialize DataLoader with filepath, and set processed flag/property to False.
        """
        pass

    def load_and_explore_data(self) -> pd.DataFrame:
        """
        Load the 311 cases dataset and return the loaded data as a pandas dataframe.

        Returns:
            pd.DataFrame: Loaded dataset as a pandas DataFrame
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If data cannot be loaded 
            KeyError: If required columns are missing
        """
        pass

    def get_basic_stats(self) -> dict[str, Any]:
        """
        Get basic statistics about the loaded dataset (shape and number of unique neighborhoods).
        
        Returns:
            Dict[str, Any]: Dictionary containing basic statistics.
            Example output:
                {
                    'shape': (1000, 15), # (Number of rows, Number of columns)
                    'unique_neighborhoods': 50 # Number of unique neighborhoods in the dataset
                }
            
        Raises:
            ValueError: If data hasn't been loaded yet
        """
        pass

    def filter_by_neighborhood(self, neighborhoods: list[str]) -> pd.DataFrame:
        """
        Filter data by neighborhood names, only including cases from the specified neighborhoods.
        
        Args:
            neighborhoods (List[str]): List of neighborhood names to filter by. 
            The names are case-insensitive, and neighborhoods in the list and in the 
            dataframe are both converted to lowercase for comparison.
            
        Returns:
            pd.DataFrame: Filtered dataset only including cases from the specified neighborhoods
            
        Raises:
            ValueError: If data isn't loaded yet
            ValueError: If no data matches the filter
        """
        pass

    @property
    def is_processed(self) -> bool:
        """
        Check if data has been processed. ie. If it has been loaded with load_and_explore_data.
        """
        pass

    @property
    def filepath(self) -> str:
        """
        Get the file path used to initialize the DataLoader.
        
        Returns:
            str: File path of the dataset
        """
        pass
