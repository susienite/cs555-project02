from helper import *

def check_correct_gender_for_role(indi_data, fam_data, errors):
    for fam in fam_data:
        roles = {'HusbandId': 'M', 'WifeId': 'F'}
        for role in roles:
            indi = getIndiById(indi_data, fam[role])
            if(indi["Gender"] != roles[role]):
                errors.append(f'ERROR: FAMILY: US21: {indi["Name"]}\'s gender {indi["Gender"]} does not match their role. It should be {roles[role]}.')