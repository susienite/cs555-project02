from helper import *

def check_marriage_before_death(indi_data, fam_data, errors):
    for fam in fam_data:
        if (fam['Married'] == 'NA'):
            continue
        else :
            husb = fam['HusbandId']
            wife = fam['WifeId']
            marr_date = fam['Married']
            husb_death = getIndiById(indi_data, husb)['Death']
            wife_death = getIndiById(indi_data, wife)['Death']
        
        #They are married, check if each death before marriage date
        if (husb_death != 'NA' and (compareDates(husb_death, marr_date) == -1)):
            husb_name = getIndiById(indi_data, husb)['Name']
            errors.append(f'ERROR: INDIVIDUAL: US05: death date ({husb_death}) of husband ({husb_name}) occurs before marriage date ({marr_date})')
        
        if (wife_death != 'NA' and (compareDates(wife_death, marr_date) == -1)):
            wife_name = getIndiById(indi_data, wife)['Name']
            errors.append(f'ERROR: INDIVIDUAL: US05: death date ({wife_death}) of wife ({wife_name}) occurs before marriage date ({marr_date})')       