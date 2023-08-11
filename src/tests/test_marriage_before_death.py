import unittest

f_no_error = "./test_geds/My-fam.ged"
f_errors = "./test_geds/marr-before-death.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.marriage_before_death import check_marriage_before_death

#test cases here.

class TestMarriageBeforeDeath(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        
    def tearDown(self): 
        self.errors = []
    
    def test_num_errors(self):
        self.prep(f_errors)
        check_marriage_before_death(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 3)  
    
    def test_error_1(self):
        self.prep(f_errors)
        check_marriage_before_death(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[0], "ERROR: INDIVIDUAL: US05: death date (1965-11-13) of husband (George /Zheng/) occurs before marriage date (1991-08-10)")
   
    def test_error_2(self):
        self.prep(f_errors)
        check_marriage_before_death(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[1], "ERROR: INDIVIDUAL: US05: death date (1965-11-13) of husband (Tyler /Ma/) occurs before marriage date (2020-03-01)" )

    def test_error_3(self):
        self.prep(f_errors)
        check_marriage_before_death(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[2], "ERROR: INDIVIDUAL: US05: death date (2000-11-13) of wife (Chloe /Ma/) occurs before marriage date (2020-03-01)" )

    def test_no_errors(self):
        self.prep(f_no_error)
        check_marriage_before_death(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()