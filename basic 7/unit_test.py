#  A function to test 

import unittest
from test_function_1 import get_formated_name
class NamesTestCase(unittest.TestCase):
    # Test for test_function_1.py
    def test_first_last_name(self):
        # Test first & last name 
        formated_name = get_formated_name('suchana','suchi')
        self.assertEqual(formated_name,'Suchana Suchi')
unittest.main()