import unittest
import sys
sys.path.append("../")
from A3parser import parser   
from stories.dates_before_current import check_dates_before_curr

#files to test
no_error = "./test_geds/My-fam.ged"
errors = "./test_geds/dates-after-current.ged"

class TestDatesBeforeCurrent(unittest.TestCase):

    def start(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = [] 
    
    def test_error_0(self):
        self.start(no_error)
        check_dates_before_curr(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 0)

    def test_error_1(self):
        self.start(errors)
        check_dates_before_curr(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(len(self.errors), 4)
    
    def test_error_2(self):
        self.start(errors)
        check_dates_before_curr(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[0], 'ERROR: INDIVIDUAL: US01: (I1): Birthday (2023-09-23) occurs in the future')
    
    def test_error_3(self):
        self.start(errors)
        check_dates_before_curr(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[1], 'ERROR: INDIVIDUAL: US01: (I5): Death (2024-06-05) occurs in the future')
    
    def test_error_4(self):
        self.start(errors)
        check_dates_before_curr(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[2], 'ERROR: INDIVIDUAL: US01: (F3): Marriage (2026-09-25) occurs in the future')
    
    def test_error_5(self):
        self.start(errors)
        check_dates_before_curr(self.indi_data, self.fam_data, self.errors)
        self.assertEqual(self.errors[3], 'ERROR: INDIVIDUAL: US01: (F4): Divorce (2029-01-12) occurs in the future')    

if __name__ == '__main__':
    unittest.main()
    





