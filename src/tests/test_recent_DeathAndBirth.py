import unittest

f_no_error = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/recent-death-and-birth.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.list_recent_deaths_and_births import make_list_of_recent

#test cases here.

class TestRecentDeathAndBirth_new(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)   
    
    def test_2Death_errors(self):
        self.prep(f_errors)
        list1 = make_list_of_recent(self.indi_data, "Death")
        self.assertEqual(len(list1)-1, 2)  
    
    def test_2Birth_errors(self):
        self.prep(f_errors)
        list2 = make_list_of_recent(self.indi_data, "Birthday")
        self.assertEqual(len(list2)-1, 2)  
    
    def test_headings(self):
        self.prep(f_errors)
        list1 = make_list_of_recent(self.indi_data, "Death")
        list2 = make_list_of_recent(self.indi_data, "Birthday")
        self.assertEqual(list1[0], "List of Recent Deaths (within last 30 days):")
        self.assertEqual(list2[0], "List of Recent Births (within last 30 days):")
    
    def test_error_1Death(self):
        self.prep(f_errors)
        list1 = make_list_of_recent(self.indi_data, "Death")
        self.assertEqual(list1[1], "\tSam /Chen/'s Death is 2023-06-28")
    
    def test_error_2Death(self):
        self.prep(f_errors)
        list1 = make_list_of_recent(self.indi_data, "Death")
        self.assertEqual(list1[2], "\tGeorge /Zheng/'s Death is 2023-07-12")
    
    def test_error_1Birth(self):
        self.prep(f_errors)
        list2 = make_list_of_recent(self.indi_data, "Birthday")
        self.assertEqual(list2[1], "\tEmily /Li/'s Birth is 2023-07-01")
    
    def test_error_2Death(self):
        self.prep(f_errors)
        list2 = make_list_of_recent(self.indi_data, "Birthday")
        self.assertEqual(list2[2], "\tEmerald /Li/'s Birth is 2023-07-01")

if __name__ == '__main__':
    unittest.main()