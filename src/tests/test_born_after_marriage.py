import unittest

f_no_error = "./test_geds/My-fam.ged"
f_no_error2 = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/born-before-marriage.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.check_born_after_marriage import check_born_after_marriage

#test cases here.
class TestParentsTooOld(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.anomalies = []   
        
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.anomalies = []
    
    def test_two_errors(self):
        self.prep(f_errors)
        check_born_after_marriage(self.indi_data, self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 2)

    def test_error_1(self):
        self.prep(f_errors)
        check_born_after_marriage(self.indi_data, self.fam_data, self.anomalies)
        self.assertEqual(self.anomalies[0], "ANOMALY: INDIVIDUAL: US09 Bob Zheng born 1970-06-04 before marriage on 1970-07-10")

    def test_error_2(self):
        self.prep(f_errors)
        check_born_after_marriage(self.indi_data, self.fam_data, self.anomalies)
        self.assertEqual(self.anomalies[1], "ANOMALY: INDIVIDUAL: US09 Jenny Zheng born 1970-01-12 before marriage on 1970-04-14")

    def test_no_errors(self):
        self.prep(f_no_error)
        check_born_after_marriage(self.indi_data, self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_born_after_marriage(self.indi_data, self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 0)

if __name__ == '__main__':
    unittest.main()