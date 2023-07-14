import unittest

f_no_error = "./test_geds/Issac-fam.ged"
f_errors = "./test_geds/My-fam.ged"

#make src/ visible for import
import sys
sys.path.append("../")

from A3parser import parser
from stories.list_living_married import list_married_living

#test cases here.

class TestMarriedLiving(unittest.TestCase):
    def prep(self, filepath): 
        self.indi_data, self.fam_data = parser(filepath)   
    
    def test_no_errors(self):
        self.prep(f_no_error)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(len(list1)-1, 0)  

    def test_errors(self):
        self.prep(f_errors)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(len(list1)-1, 4) 

    def test_headings(self):
        self.prep(f_errors)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(list1[0], "List of Married Living Individuals:")

    def test_error_1(self):
        self.prep(f_errors)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(list1[1], "\tZach /Tan/ and Winnie /Chen/ are married and living")

    def test_error_2(self):
        self.prep(f_errors)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(list1[2], "\tSam /Chen/ and Julia /Kim/ are married and living")
        
    def test_error_3(self):
        self.prep(f_errors)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(list1[3], "\tDavid /Li/ and Bonnie /Chen/ are married and living")
        
    def test_error_4(self):
        self.prep(f_errors)
        list1 = list_married_living(self.indi_data, self.fam_data)
        self.assertEqual(list1[4], "\tTyler /Ma/ and Chloe /Ma/ are married and living")

if __name__ == '__main__':
    unittest.main()