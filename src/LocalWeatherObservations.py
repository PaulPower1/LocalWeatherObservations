"""
    Name        : LocalWeatherObservations.py
    Author      : Paul Power
    Created     : 24-Aug-2024

    Description : This program returns the weather from a publicly available API for a given location.  
                  All temps are converted from kelvin to celsius and fahrenheit
 
"""

"""
Todos:
    1. Take a list of suburbs to report weather obs for and output json to either file or console
    2. Develop a UI to enter parameters and present responses  
    3. Allow setting of a timer to automate how frequently and how many iterations to report on (e.g vmstat)
    4. After getting above working make a cloud API for this and run from Azure/AWS    
"""

import argparse
from collections import namedtuple
import json

#define a namedtuple for the location
Location = namedtuple("Location", ["latitude", "longitude"])

def create_parser() -> list[str]:
    #create a docstring for this function with paramaters and returns
    """
    Create a parser to parse the command-line arguments

    Returns:
        list: A list of the parsed arguments
    """

    # Create the ArgumentParser object
    parser = argparse.ArgumentParser(description="Process a comma-separated list")

    # Add an argument that takes a comma-separated list
    parser.add_argument("--items", 
                        type=str, 
                        default="", 
                        help="A comma-separated list of items")

    # Parse the arguments
    return parser.parse_args()

def process_args(args:argparse.Namespace) -> list[str]: # Split the comma-separated list into individual items and cleanup
    return [item.strip() for item in args.items.split(",") if args.items]


def get_locations(locations:str) -> dict:
    #create a docstring for this function with paramaters and returns
    """
    Get the locations from the user

    Returns:
        dict: A dictionary of the locations
    """
    # Parse function param and generate a list of locations
    location_list = locations.split(",")

    # Create a dictionary to hold the locations
    locations = {}

    for location in location_list:
        # call out to the weatherapi and get coords
                
        # add to the dictionary 
        # return dictionary aas  

        # Add the location to the dictionary
        # use a namedtuple for lat and long
        latitude=0
        longitude=0

        locations[location] = Location(latitude, longitude)

    # Return the dictionary of locations
    # return locations.dumps()
    return locations

    
def main():
    print(process_args(create_parser()))

if __name__ == "__main__":
    main()