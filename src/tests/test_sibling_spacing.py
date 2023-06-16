import unittest

f_no_error = "./test_geds/My-fam.ged"
f_no_error2 = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/sibling-space-too-close.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.check_sibling_spacing import check_sibling_spacing

#test cases here.

class TestSiblingSpacing(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.errors = []
    
    def test_two_errors(self):
        self.prep(f_errors)
        check_sibling_spacing(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 1)

    def test_error_1(self):
        self.prep(f_errors)
        check_sibling_spacing(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[0], "ANOMALY: FAMILY: US13: The birth dates of siblings Ryan Zheng (I8) and Bob Zheng (I1) are incorrectly spaced.")

    def test_no_errors(self):
        self.prep(f_no_error)
        check_sibling_spacing(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_sibling_spacing(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()