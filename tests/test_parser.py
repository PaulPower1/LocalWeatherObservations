# test_parser.py
import unittest
from unittest import mock

import sys
import os
import argparse

sys.path.append("./src")

import LocalWeatherObservations as lwo
from LocalWeatherObservations import * 

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--items', nargs=1, type=str, help='List of two items')
    return parser.parse_args()  # This should return the parsed arguments

class TestArgParse(unittest.TestCase):
    
    @mock.patch('argparse.ArgumentParser.parse_args', 
                return_value=argparse.Namespace(items="melbourne, stkilda"))
    def test_valid_arguments(self, mock_parse_args):
        args_items = create_parser()  # This will use the mocked parse_args method
        
        args = lwo.process_args(args_items)
        
        # Assert the parsed values
        self.assertEqual(args[0], "melbourne")
        self.assertEqual(args[1], "stkilda")
        
if __name__ == "__main__":
    unittest.main()