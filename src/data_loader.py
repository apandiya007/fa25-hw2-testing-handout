"""
data_loader.py
Module responsible for loading and basic exploration of 311 cases dataset.
Follows single responsibility principle: handles data input and initial exploration.
"""
from typing import Any

import pandas as pd
import os

class DataLoader:
    """
    Class for loading and managing 311 cases data.
    """

    def __init__(self, filepath: str):
        """
        Initialize DataLoader with filepath, and set processed flag/property to False.
        """
        if not isinstance(filepath, str) or not filepath:
            raise ValueError("Filepath must be a non-empty string")
        self._filepath = filepath
        self._data: pd.DataFrame | None = None
        self._processed: bool = False

    def load_and_explore_data(self) -> pd.DataFrame:
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self._filepath}")       
        try:
            df = pd.read_csv(self._filepath)
        except Exception as e:
            raise ValueError(f"Could not load data: {e}") from e
        # validates requires columns
        required_columns = {"neighborhood"}
        df_columns_lower = set(df.columns.str.lower())
        missing = required_columns - df_columns_lower
        if missing:
            raise KeyError(f"Missing required columns: {missing}")
        self._data = df
        self._processed = True
        return self._data                            
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
        if self._data is None or not self._processed:
            raise ValueError("Data has not been loaded yet")
        stats = {
            "shape": self._data.shape,
            "unique_neighborhoods": self._data["neighborhood"].nunique()
        }
        return stats   

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
        if self._data is None or not self._processed:
            raise ValueError("Data has not been loaded yet")        
        if "neighborhood" not in self._data.columns:
            raise KeyError("Missing required column: neighborhood")
       
        neighborhoods_lower = [n.lower() for n in neighborhoods]
        filtered = self._data[
            self._data["neighborhood"].str.lower().isin(neighborhoods_lower)

        ]

        if filtered.empty:
            raise ValueError("No data matches the filter")
        
        return filtered
    


    @property
    def is_processed(self) -> bool:
        """
        Check if data has been processed. ie. If it has been loaded with load_and_explore_data.
        """
        return self._processed

    @property
    def filepath(self) -> str:
        """
        Get the file path used to initialize the DataLoader.
        
        Returns:
            str: File path of the dataset
        """
        return self._filepath
