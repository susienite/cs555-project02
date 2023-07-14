import unittest

f_no_error = "./test_geds/Issac-fam.ged"
f_no_error2 = "./test_geds/death-before-marriage.ged"
f_errors = "./test_geds/death-and-birth-before-marriage.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.birth_before_marriage import check_birth_before_marriage

#test cases here.

class TestBirthBeforeMarriage(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.errors = []
    
    def test_two_errors(self):
        self.prep(f_errors)
        check_birth_before_marriage(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 2)

    def test_error_1(self):
        self.prep(f_errors)
        check_birth_before_marriage(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[0], "ERROR: INDIVIDUAL: US08: Birth date (1970-04-14) of Angela Zheng (I7) occurs on the same day or after her marriage date (1970-04-14)")

    def test_error_2(self):
        self.prep(f_errors)
        check_birth_before_marriage(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[1], "ERROR: INDIVIDUAL: US08: Birth date (1999-08-08) of Kelly Peng /Peng/ (I9) occurs on the same day or after her marriage date (1998-05-08)")

    def test_no_errors(self):
        self.prep(f_no_error)
        check_birth_before_marriage(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_birth_before_marriage(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()