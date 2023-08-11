import unittest

# Test files
f_no_error = "./test_geds/my-fam.ged"
f_errors_cousins = "./test_geds/first-cousins-are-married.ged"

import sys
sys.path.append("../")

from A3parser import parser
from stories.check_first_cousins_should_not_marry import check_first_cousins_should_not_marry 

class TestCousinMarriage(unittest.TestCase):

    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        self.anomalies = []

    def tearDown(self):  # Reset errors after each test
        self.anomalies = []

    def test_no_errors(self):
        self.prep(f_no_error)
        check_first_cousins_should_not_marry(self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 0)

    def test_errors(self):
        self.prep(f_errors_cousins)
        check_first_cousins_should_not_marry(self.fam_data, self.anomalies)
        self.assertEqual(self.anomalies[0], "ANOMALY: FAMILY: US19: Dani /Tan/ (I1) and Bonnie /Chen/ (I7) are first cousins and should not be married.")

if __name__ == '__main__':
    unittest.main()
