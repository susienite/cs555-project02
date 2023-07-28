import unittest

f_no_error = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/death-before-birth.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.birth_before_death import check_birth_before_death

#test cases here.

class TestBirthBeforeDeath(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.errors = []
    
    def test_errors(self):
        self.prep(f_errors)
        check_birth_before_death(self.indi_data, self.errors)
        self.assertEqual(len(self.errors), 2)
    
    def test_error_1(self):
        self.prep(f_errors)
        check_birth_before_death(self.indi_data, self.errors)
        self.assertEqual(self.errors[0],"ERROR: INDIVIDUAL: US03: Birth date (1950-09-06) of Timmy Zheng (I4) occurs on the same day or after Death date (1949-06-07)")

    def test_error_2(self):
        self.prep(f_errors)
        check_birth_before_death(self.indi_data, self.errors)
        self.assertEqual(self.errors[1],"ERROR: INDIVIDUAL: US03: Birth date (1920-04-05) of Kelly Peng /Peng/ (I9) occurs on the same day or after Death date (1002-05-03)")
    
    def test_no_error1(self):
        self.prep(f_no_error)
        check_birth_before_death(self.indi_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()



    
