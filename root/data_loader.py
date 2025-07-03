"""
data_loader.py
Module responsible for loading and basic exploration of 311 cases dataset.
Follows single responsibility principle: handles data input and initial exploration.

BUGGY VERSION FOR HW2 - Students need to write tests to debug this code!
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any

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
        self.filepath = filepath
        self._data = None  # Private attribute - should not be accessed directly
        self.__processed = False  # Private attribute for internal state
        
    def load_and_explore_data(self) -> pd.DataFrame:
        """
        Load the 311 cases dataset and display basic information.
        
        Returns:
            pd.DataFrame: Loaded dataset
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If data cannot be loaded
        """
        try:
            # BUG 1: Wrong delimiter used - should be ',' but using ';'
            self._data = pd.read_csv(self.filepath, delimiter=';')
            
            print(f"Dataset loaded successfully!")
            print(f"Shape: {self._data.shape}")
            print(f"Columns: {list(self._data.columns)}")
            
            # BUG 2: Accessing private method from wrong context
            self._validate_required_columns()
            
            self.__processed = True
            return self._data
            
        except Exception as e:
            raise ValueError(f"Could not load data: {str(e)}")
    
    def _validate_required_columns(self) -> bool:
        """
        Private method to validate that required columns exist.
        Should only be called internally.
        
        Returns:
            bool: True if all required columns exist
            
        Raises:
            KeyError: If required columns are missing
        """
        required_cols = ['case_enquiry_id', 'open_dt', 'target_dt', 
                        'closed_dt', 'category', 'latitude', 'longitude', 
                        'neighborhood']
        
        missing_cols = []
        for col in required_cols:
            if col not in self._data.columns:
                missing_cols.append(col)
        
        if missing_cols:
            raise KeyError(f"Missing required columns: {missing_cols}")
        
        return True
    
    def get_basic_stats(self) -> Dict[str, Any]:
        """
        Get basic statistics about the loaded dataset.
        
        Returns:
            Dict[str, Any]: Dictionary containing basic statistics
            
        Raises:
            ValueError: If data hasn't been loaded yet
        """
        if self._data is None:
            raise ValueError("Data must be loaded first using load_and_explore_data()")
        
        # BUG 3: Wrong method call - should be .describe() not .summary()
        stats = {
            'shape': self._data.shape,
            'summary': self._data.summary(),  # This will cause AttributeError
            'null_counts': self._data.isnull().sum(),
            'unique_neighborhoods': len(self._data['neighborhood'].unique())
        }
        
        return stats
    
    def filter_by_city(self, cities: List[str]) -> pd.DataFrame:
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
        # BUG 4: Type mismatch - expecting List[str] but might receive str
        if isinstance(cities, str):
            # Should raise TypeError but instead tries to convert
            cities = cities.split(',')  # This causes issues with single city names
        
        if self._data is None:
            raise ValueError("Data must be loaded first")
        
        # BUG 5: Case-sensitive comparison when data might have mixed case
        filtered_data = self._data[self._data['city'].isin(cities)]
        
        if len(filtered_data) == 0:
            raise ValueError(f"No data found for cities: {cities}")
        
        return filtered_data
    
    @property
    def is_processed(self) -> bool:
        """
        Check if data has been processed.
        
        Returns:
            bool: True if data is processed
        """
        return self.__processed
    
    def _get_raw_data(self) -> pd.DataFrame:
        """
        Private method to get raw data - should not be called externally.
        
        Returns:
            pd.DataFrame: Raw dataset
        """
        return self._data


def load_and_explore_data(filepath: str) -> pd.DataFrame:
    """
    Legacy function for backward compatibility.
    Load the 311 cases dataset and display basic information.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    loader = DataLoader(filepath)
    return loader.load_and_explore_data()