from helper import *

def check_marriage_after_14(indi_data, fam_data, errors):
    for fam in fam_data:
        husb_data = getIndiById(indi_data, fam['HusbandId'])
        wife_data = getIndiById(indi_data, fam['WifeId'])
        if(fam['Married'] == 'NA'): continue #TODO: handle NA dates -> "The four records that require a date (BIRT, DEAT, DIV, MARR) will always befollowed by a DATE record. " might be able to just get away with continuing
        if(husb_data['Age'] < 14):
            errors.append(f'ERROR: INDIVIDUAL: US10: {husb_data["Name"]} ({husb_data["ID"]}) married before 14 at {husb_data["Age"]}')
        if(wife_data['Age'] < 14):
            errors.append(f'ERROR: INDIVIDUAL: US10: {wife_data["Name"]} ({wife_data["ID"]}) married before 14 at {wife_data["Age"]}')
