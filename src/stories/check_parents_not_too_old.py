from helper import *

def check_parents_not_too_old(indi_data, fam_data, anomalies):
    for fam in fam_data:
        husb_data = getIndiById(indi_data, fam['HusbandId'])
        wife_data = getIndiById(indi_data, fam['WifeId'])
        for child_id in fam['Children']:
            child_data = getIndiById(indi_data, child_id)
            if child_data is None or husb_data is None or wife_data is None:
                continue
            #calculate the age difference
            if husb_data['Birthday'] != 'NA' and child_data['Birthday'] != 'NA':
                husb_birth = datetime.strptime(husb_data['Birthday'], '%Y-%m-%d').date()
                child_birth = datetime.strptime(child_data['Birthday'], '%Y-%m-%d').date()
                # age_difference_husb = computeAgeFromDeath(child_birth, husb_birth)
                age_difference_husb = computeAgeDifferenceInYears(child_birth, husb_birth)
                if age_difference_husb > 80:
                    anomalies.append(f'ANOMALY: FAMILY: US12: {fam["ID"]}: Father ({husb_data["ID"]}) is more than 80 years older than child ({child_data["ID"]})')
            if wife_data['Birthday'] != 'NA' and child_data['Birthday'] != 'NA':
                wife_birth = datetime.strptime(wife_data['Birthday'], '%Y-%m-%d').date()
                child_birth = datetime.strptime(child_data['Birthday'], '%Y-%m-%d').date()
                # age_difference_wife = computeAgeFromDeath(child_birth, wife_birth)
                age_difference_wife = computeAgeDifferenceInYears(child_birth, wife_birth)
                if age_difference_wife > 60:
                    anomalies.append(f'ANOMALY: FAMILY: US12: {fam["ID"]}: Mother ({wife_data["ID"]}) is more than 60 years older than child ({child_data["ID"]})')
