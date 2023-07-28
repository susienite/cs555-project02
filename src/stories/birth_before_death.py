from helper import *

def check_birth_before_death(indi_data, errors):
    for person in indi_data:
        Bday = person['Birthday']
        Dday = person['Death']
        if (Bday != 'NA' and Dday != 'NA') :
            if(compareDates(Bday, Dday) != -1):
                errors.append(f'ERROR: INDIVIDUAL: US03: Birth date ({Bday}) of {person["Name"]} ({person["ID"]}) occurs on the same day or after Death date ({Dday})')
        