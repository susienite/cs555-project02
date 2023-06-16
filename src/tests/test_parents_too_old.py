import unittest

f_no_error = "./test_geds/My-fam.ged"
f_no_error2 = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/parent-too-old.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.check_parents_not_too_old import check_parents_not_too_old

#test cases here.

class TestParentsTooOld(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.errors = []
    
    def test_two_errors(self):
        self.prep(f_errors)
        check_parents_not_too_old(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 2)

    def test_error_1(self):
        self.prep(f_errors)
        check_parents_not_too_old(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[0], "ANOMALY: FAMILY: US08: F4: Father (I8) is more than 80 years older than child (I11)")

    def test_error_2(self):
        self.prep(f_errors)
        check_parents_not_too_old(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[1], "ANOMALY: FAMILY: US08: F4: Mother (I10) is more than 60 years older than child (I11)")

    def test_no_errors(self):
        self.prep(f_no_error)
        check_parents_not_too_old(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_parents_not_too_old(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()