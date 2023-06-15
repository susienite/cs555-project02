from helper import *

def check_birth_before_marriage(indi_data, fam_data, errors):
    for fam in fam_data:
        husb_data = getIndiById(indi_data, fam['HusbandId'])
        wife_data = getIndiById(indi_data, fam['WifeId'])
        if(husb_data['Birthday'] == 'NA' or wife_data['Birthday'] == 'NA' or fam['Married'] == 'NA'): continue #TODO: how to handle NA dates?
        if(compareDates(husb_data['Birthday'], fam['Married']) != -1):
            errors.append(f'ERROR: INDIVIDUAL: US08: Birth date ({husb_data["Birthday"]}) of {husb_data["Name"]} ({husb_data["ID"]}) occurs on the same day or after his marriage date ({fam["Married"]})')
        if(compareDates(wife_data['Birthday'], fam['Married']) != -1):
            errors.append(f'ERROR: INDIVIDUAL: US08: Birth date ({wife_data["Birthday"]}) of {wife_data["Name"]} ({wife_data["ID"]}) occurs on the same day or after her marriage ({fam["Married"]})')
