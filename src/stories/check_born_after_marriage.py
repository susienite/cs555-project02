from helper import *

def check_born_after_marriage(indi_data, fam_data, anomalies):
    for fam in fam_data:
        for child in fam['Children']:
            child = getIndiById(indi_data, child)
            if child['Birthday'] < fam['Married']:
                anomalies.append(f'ANOMALY: INDIVIDUAL: US09 {child["Name"]} born {child["Birthday"]} before marriage on {fam["Married"]}')