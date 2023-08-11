from helper import *

def check_male_last_names(indi_data, fam_data, errors):
    for fam in fam_data:
        last_name = fam['HusbandName'].split(' ')[1]
        for child_id in fam['Children']:
            child = getIndiById(indi_data, child_id)
            if(child['Gender'] == "M" and child['Name'].split(' ')[1] != last_name):
                errors.append(f'ERROR: FAMILY: US16: {child["Name"]} of {fam["ID"]} has a different last name than their father')