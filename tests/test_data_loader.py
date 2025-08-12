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
        pass

    def test_load_and_explore_data_success(self) -> None:
        """Test successful data loading."""
        # Write test to load valid CSV file
        # Check if data loads correctly. This test has been written for you.
        # You may use this as a template for your other tests that involve checking
        # equality of a pandas DataFrame.
        loader = DataLoader("example_CSVs/311_Cases_SF_Sample.csv")
        loaded_data = loader.load_and_explore_data()
        data = [
            [18310793, "Open", "Graffiti", "HAIGHT ST", 5, "Buena Vista", "PARK",
             37.770346666667, -122.443505, "(37.77034667, -122.443505)",
             "POINT (-122.443505 37.770346667)", "2024-06-06T07:00:00.000Z",
             "2025-05-20T07:00:00.000Z", 348, True, 38302, 38302],
            [101001847422, "Open", "General Request", "NANTUCKET AVE", 11,
             "Mission Terrace", "INGLESIDE", 37.72837489, -122.44197876,
             "(37.72837489, -122.44197876)", "POINT (-122.44197876 37.72837489)",
             "2025-04-30T07:00:00.000Z", "2025-05-20T07:00:00.000Z", 20, True,
             100757, 100757],
            [17744268, "Open", "General Request - MTA", "OFARRELL ST", 5,
             "Tenderloin", "TENDERLOIN", 37.785694, -122.415016,
             "(37.785694, -122.415016)", "POINT (-122.415016 37.785694)",
             "2024-01-08T08:00:00.000Z", "2025-05-20T07:00:00.000Z", 498, True,
             53734, 53734],
            [16987951, "Open", "Shared Spaces Violation", "46TH AVE", 4,
             "Outer Sunset", "TARAVAL", 37.764021424039, -122.506313033794,
             "(37.76402142, -122.50631303)", "POINT (-122.506313034 37.764021424)",
             "2023-07-01T07:00:00.000Z", "2025-05-20T07:00:00.000Z", 689, True,
             21957, 21957],
            [18126205, "Open", "Graffiti", "PRESIDIO AVE", 2,
             "Laurel Heights / Jordan Park", "RICHMOND", 0, 0, "(0.0, 0.0)",
             "POINT (0 0)", "2024-04-18T07:00:00.000Z", "2025-05-20T07:00:00.000Z",
             397, True, 69544, 69544],
            [16957912, "Open", "Rec and Park Requests", "17TH ST", 9,
             "Mission", "MISSION", 37.764546816915, -122.409804426134,
             "(37.76454682, -122.40980443)", "POINT (-122.409804426 37.764546817)",
             "2023-06-24T07:00:00.000Z", "2025-05-20T07:00:00.000Z", 696, True,
             58698, 58698],
            [18329037, "Open", "Encampments", "VAN NESS AVE", 2,
             "Pacific Heights", "NORTHERN", 37.797523997093, -122.424043933063,
             "(37.797524, -122.42404393)", "POINT (-122.424043933 37.797523997)",
             "2024-06-11T07:00:00.000Z", "2025-05-20T07:00:00.000Z", 343, True,
             13028, 13028],
            [16831546, "Open", "General Request - PUBLIC WORKS", "THORNTON AVE",
             10, "Silver Terrace", "BAYVIEW", 37.731252713164, -122.39615902316,
             "(37.73125271, -122.39615902)", "POINT (-122.396159023 37.731252713)",
             "2023-05-24T07:00:00.000Z", "2025-05-20T07:00:00.000Z", 727, True,
             79423, 79423],
            [16856081, "Open", "Street and Sidewalk Cleaning", "LARKIN ST", 3,
             "Lower Nob Hill", "CENTRAL", 37.788176670463, -122.418483462817,
             "(37.78817667, -122.41848346)", "POINT (-122.418483463 37.78817667)",
             "2023-05-31T07:00:00.000Z", "2025-05-20T07:00:00.000Z", 720, True,
             59050, 59050],
            [16948615, "Open", "General Request - MTA", "PRESIDIO AVE", 2,
             "Laurel Heights / Jordan Park", "RICHMOND", 0, 0, "(0.0, 0.0)",
             "POINT (0 0)", "2023-06-22T07:00:00.000Z", "2025-05-20T07:00:00.000Z",
             698, True, 50193, 50193]
        ]

        columns = [
            "CaseID", "Status", "Category", "Street", "Supervisor District", "Neighborhood",
            "Police District", "Latitude", "Longitude", "Point", "point_geom",
            "OpenedDate", "ClosedDate", "days_open", "selected", "__seqId", "__i/0"
        ]

        expected_df = pd.DataFrame(data, columns=columns)


        self.assertTrue(loaded_data.equals(expected_df))


    def test_load_nonexistent_file(self) -> None:
        """Test loading non-existent file."""
        # Write test for loading non-existent file
        pass

    def test_load_bad_file_format(self) -> None:
        """Test loading file with bad format."""
        # Write test for loading file with bad format,
        # using the provided bad_file_format.zip file.
        pass

    def test_validate_required_columns_missing(self) -> None:
        """Test column validation with missing required columns."""
        # Write test for loading a csv with missing required columns,
        # using the provided 311_Cases_missing_CaseID.csv file.
        pass

    def test_get_basic_stats_without_loading(self) -> None:
        """Test getting stats before loading data."""
        # Write test for trying to get basic stats before loading data
        pass

    def test_get_basic_stats_success(self) -> None:
        """Test getting basic stats after loading data."""
        # Write test for successful stats retrieval
        # Load the data, and check if stats contain expected keys and values
        pass

    def test_filter_by_neighborhood_list_input(self) -> None:
        """Test filtering by city with list input."""
        # Write test for filtering with list of neighborhoods
        pass

    def test_filter_by_neighborhood_case_insensitive(self) -> None:
        """Test filtering by city with different case."""
        # Write test for case-insensitive filtering
        # Should work regardless of case
        # Write test for filtering with list of neighborhoods
        pass

    def test_filter_by_neighborhood_no_matches(self) -> None:
        """Test filtering by neighborhood with no matches."""
        # Write test for no matching cities
        pass

    def test_filter_by_neighborhood_without_loading(self) -> None:
        """Test filtering before loading data."""
        # Write test for filtering before loading
        pass
