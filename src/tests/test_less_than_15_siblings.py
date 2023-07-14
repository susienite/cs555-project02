import unittest

f_no_error2 = "./test_geds/My-fam.ged"
f_no_error = "./test_geds/Issac-fam.ged"
f_anomalies = "./test_geds/too_many_siblings.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.check_less_than_15_siblings import check_less_than_15_siblings

#test cases here.

class TestMarriageBeforeDivorce(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.anomalies = []    
        
    def tearDown(self): 
        self.anomalies = []
    
    def test_one_errors(self):
        self.prep(f_anomalies)
        check_less_than_15_siblings(self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 1)  
    
    def test_error_1(self):
        self.prep(f_anomalies)
        check_less_than_15_siblings(self.fam_data, self.anomalies)
        self.assertEqual(self.anomalies[0], "ANOMALY: FAMILY: US15: Bob Zheng and Jenny Zheng of F1 have more than 15 children (that are siblings)!")
   
    def test_no_errors(self):
        self.prep(f_no_error)
        check_less_than_15_siblings(self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 0)
        
    def test_no_errors2(self):
        self.prep(f_no_error2)
        check_less_than_15_siblings(self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 0)

if __name__ == '__main__':
    unittest.main()