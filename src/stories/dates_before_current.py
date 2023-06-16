from helper import *

def check_dates_before_curr(indi_data, fam_data, errors):
    for person in indi_data:
        if (person['Birthday'] != 'NA' and compareDates(person['Birthday'], getToday()) > 0): 
            errors.append(f'ERROR: INDIVIDUAL: US01: ({person["ID"]}): Birthday ({person["Birthday"]}) occurs in the future')
        if (person['Death'] != 'NA' and compareDates(person['Death'], getToday()) > 0):
                errors.append(f'ERROR: INDIVIDUAL: US01: ({person["ID"]}): Death ({person["Death"]}) occurs in the future')
    for fam in fam_data:
        if (fam['Married'] != 'NA' and compareDates(fam['Married'], getToday()) > 0): 
            errors.append(f'ERROR: INDIVIDUAL: US01: ({fam["ID"]}): Marriage ({fam["Married"]}) occurs in the future')
        if (fam['Divorced'] != 'NA' and compareDates(fam['Divorced'], getToday()) > 0):
                errors.append(f'ERROR: INDIVIDUAL: US01: ({fam["ID"]}): Divorce ({fam["Divorced"]}) occurs in the future')



        


