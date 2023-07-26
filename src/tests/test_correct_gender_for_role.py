import unittest

f_no_error = "./test_geds/My-fam.ged"
f_no_error2 = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/incorrect-gender-for-role.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.correct_gender_for_role import check_correct_gender_for_role

#test cases here.
class TestParentsTooOld(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        self.anomalies = []
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.errors = []
        self.anomalies = []
    
    def test_two_errors(self):
        self.prep(f_errors)
        check_correct_gender_for_role(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 2)

    def test_error_1(self):
        self.prep(f_errors)
        check_correct_gender_for_role(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[0], "ERROR: FAMILY: US21: Joe Zheng's gender F does not match their role. It should be M.")

    def test_error_2(self):
        self.prep(f_errors)
        check_correct_gender_for_role(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[1], "ERROR: FAMILY: US21: Kelly Peng /Peng/'s gender M does not match their role. It should be F.")

    def test_no_errors(self):
        self.prep(f_no_error)
        check_correct_gender_for_role(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_correct_gender_for_role(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

if __name__ == '__main__':
    unittest.main()