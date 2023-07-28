from helper import *

def check_unique_ids(indi_data, fam_data, errors):
    dict = {}
    for indi in indi_data:
        if(dict.get(indi['ID']) != None):
            errors.append(f'ERROR: INDIVIDUAL: US22: {indi["ID"]} is not unique')
        dict[indi['ID']] = 1
    for fam in fam_data:
        if(dict.get(fam['ID']) != None):
            errors.append(f'ERROR: FAMILY: US22: {fam["ID"]} is not unique')
        dict[fam['ID']] = 1