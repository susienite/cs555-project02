from helper import *

def check_sibling_spacing(indi_data, fam_data, anomalies):
    for fam in fam_data:
        sibling_birthdates = []
        for child_id in fam['Children']:
            child_data = getIndiById(indi_data, child_id)
            if child_data['Birthday'] != 'NA':
                sibling_birthdates.append((child_id, child_data['Birthday']))

        sibling_birthdates.sort(key=lambda x: x[1])  #Sorting the sibling_birthdates list based on the dates

        for i in range(1, len(sibling_birthdates)):
            sibling1_id, sibling1_bday = sibling_birthdates[i - 1]
            sibling2_id, sibling2_bday = sibling_birthdates[i]
            month_diff = computeAgeDifferenceInMonths(sibling1_bday, sibling2_bday)
            day_diff = computeAgeDifferenceInDays(sibling1_bday, sibling2_bday)

            # If the siblings' birthdates are less than 8 months but more than 2 days apart, report an error
            if 2 < day_diff < 30 * 8:
                sibling1_data = getIndiById(indi_data, sibling1_id)
                sibling2_data = getIndiById(indi_data, sibling2_id)
                anomalies.append(f'ANOMALY: FAMILY: US08: The birth dates of siblings {sibling1_data["Name"]} ({sibling1_id}) and {sibling2_data["Name"]} ({sibling2_id}) are incorrectly spaced.')
