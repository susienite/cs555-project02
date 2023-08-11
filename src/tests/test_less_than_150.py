import unittest

f_no_error = "./test_geds/My-fam.ged"
f_no_error2 = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/death_over_150_yrs.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.less_than_150_age import check_less_than_150

#test cases here.
class TestParentsTooOld(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []   
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.errors = []
    
    def test_two_errors(self):
        self.prep(f_errors)
        check_less_than_150(self.indi_data, self.errors)
        self.assertEqual(len(self.errors), 2)

    def test_error_1(self):
        self.prep(f_errors)
        check_less_than_150(self.indi_data, self.errors)
        self.assertEqual(self.errors[0], "ERROR: INDIVIDUAL: US07: Timmy Zheng: died past 150 years old. Birth date 1800-09-06, Death date 2005-06-07")

    def test_error_2(self):
        self.prep(f_errors)
        check_less_than_150(self.indi_data, self.errors)
        self.assertEqual(self.errors[1], "ERROR: INDIVIDUAL: US07: Kelly Peng /Peng/: died past 150 years old. Birth date 1800-04-05, Death date 2003-07-06")

    def test_no_errors(self):
        self.prep(f_no_error)
        check_less_than_150(self.indi_data, self.errors)
        self.assertEqual(len(self.errors), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_less_than_150(self.indi_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()