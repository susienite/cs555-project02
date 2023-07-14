import unittest

f_no_error2 = "./test_geds/My-fam.ged"
f_no_error = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/recent-death-and-birth.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.OLD_list_of_recent_deaths import make_list_of_recent_deaths
from stories.OLD_list_of_recent_births import make_list_of_recent_births 

#test cases here.

class TestMarriageBeforeDivorce(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)   
    
    def test_1Death_errors(self):
        self.prep(f_no_error2)
        table1, list1 = make_list_of_recent_deaths(self.indi_data)
        self.assertEqual(len(list1), 1)  
    
    def test_2Death_errors(self):
        self.prep(f_errors)
        table1, list1 = make_list_of_recent_deaths(self.indi_data)
        self.assertEqual(len(list1), 2)  
    
    def test_2Birth_errors(self):
        self.prep(f_errors)
        table2, list2 = make_list_of_recent_births(self.indi_data)
        self.assertEqual(len(list2), 2)  
    
    def test_error_1Death(self):
        self.prep(f_errors)
        table1, list1 = make_list_of_recent_deaths(self.indi_data)
        self.assertEqual(list1[0], ['I5', 'Sam /Chen/', '2023-06-28'])
    
    def test_error_2Death(self):
        self.prep(f_errors)
        table1, list1 = make_list_of_recent_deaths(self.indi_data)
        self.assertEqual(list1[1], ['I8', 'George /Zheng/', '2023-07-12'])
    
    def test_error_1Birth(self):
        self.prep(f_errors)
        table1, list1 = make_list_of_recent_births(self.indi_data)
        self.assertEqual(list1[0], )
    
    def test_error_2Birth(self):
        self.prep(f_errors)
        table1, list1 = make_list_of_recent_births(self.indi_data)
        self.assertEqual(list1[1], )
    
    def test_no_errors(self):
        self.prep(f_no_error)
        table1, list1 = make_list_of_recent_deaths(self.indi_data)
        self.assertEqual(len(list1), 0)  
        

if __name__ == '__main__':
    unittest.main()