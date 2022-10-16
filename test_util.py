
"""
A test module to validate the Util file functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest
from datetime import datetime

import util


class TestPersonList(unittest.TestCase):

    def test_datetime_conversion(self):
        self.assertEqual(datetime(2000, 1, 1), util.convert_string_to_datetime("2000-1-1"))

    def test_wrong_datetime_conversion(self):
        with self.assertRaises(ValueError):
            util.convert_string_to_datetime("2000, 1, 1")
