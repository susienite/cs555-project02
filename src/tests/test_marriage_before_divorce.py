import unittest

f_no_error2 = "./test_geds/My-fam.ged"
f_no_error = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/marr-before-divorce.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.marriage_before_divorce2 import check_marriage_before_divorce

#test cases here.

class TestMarriageBeforeDivorce(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        
    def tearDown(self): 
        self.errors = []
    
    def test_one_errors(self):
        self.prep(f_errors)
        check_marriage_before_divorce(self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 1)  
    
    def test_error_1(self):
        self.prep(f_errors)
        check_marriage_before_divorce(self.fam_data, self.errors)
        self.assertEqual(self.errors[0], "ERROR: INDIVIDUAL: US04: Divorce of (1994-07-06) of (Ryan Zheng) and (Kelly Peng /Peng/) occurs before marriage date (1998-05-08)")
   
    def test_no_errors(self):
        self.prep(f_no_error)
        check_marriage_before_divorce(self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_marriage_before_divorce(self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()