import unittest

f_no_error = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/siblings-are-married.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.check_siblings_should_not_marry import check_siblings_should_not_marry

#test cases here.

class TestSiblingMarriage(unittest.TestCase):
    # def prep(self, filepath): 
    #     self.indi_data, self.fam_data = parser(filepath)   
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)
        self.errors = []    
        self.anomalies = []
    
    def tearDown(self): # reset errors after each test. https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.anomalies = []

    def test_no_errors(self):
        self.prep(f_no_error)
        check_siblings_should_not_marry(self.fam_data, self.anomalies)
        self.assertEqual(len(self.anomalies), 0)  
        
        # self.assertEqual(self.errors[0], "ERROR: FAMILY: US21: Joe Zheng's gender F does not match their role. It should be M.")


    def test_errors(self):
        self.prep(f_errors)
        check_siblings_should_not_marry(self.fam_data, self.anomalies)
        # print(len(self.anomalies))
        print(self.anomalies)
        self.assertEqual(self.anomalies[0], "ANOMALY: FAMILY: US18: Sam Chen ({husband_id}) and Julia Chen ({wife_id}) are siblings and should not be married. Is this Alabama?") 


        

if __name__ == '__main__':
    unittest.main()