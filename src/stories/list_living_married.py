from helper import *
from prettytable import PrettyTable

#return a list of married living people 
def list_married_living(indi_data, fam_data):
    married_living_list = []

    heading = 'List of Married Living Individuals:' 
    married_living_list.append(heading)

    for family in fam_data:
        husb = family['HusbandID']
        wife = family['WifeID']

        if husb in indi_data and wife in indi_data:
            husb_death = indi_data[husb]['Death']
            wife_death = indi_data[wife]['Death']

            if (husb_death == 'NA' or husb_death is None) and (wife_death == 'NA' or wife_death is None):
                married_living_str = "\t" + indi_data[husb]['Name'] + " and " + indi_data[wife]['Name'] + " are married and living"
                married_living_list.append(married_living_str)
    
    return married_living_list

  


