from helper import *

def check_siblings_should_not_marry(fam_data, anomalies):
    
    # Check if any married couples are siblings
    for fam in fam_data:
        husband_id = fam.get('HusbandId')
        wife_id = fam.get('WifeId')
        children = fam.get('Children', [])
        if husband_id in children and wife_id in children:
                anomalies.append(f'ANOMALY: FAMILY: US18: {fam["HusbandName"]} ({husband_id}) and {fam["WifeName"]} ({wife_id}) are siblings and should not be married. Is this Alabama?')
                # break  # Exit inner loop if anomaly found
        
        # # husband_id = fam['HusbandId']
        # # wife_id = fam['WifeId']
        # husband_id = fam.get('HusbandId')
        # wife_id = fam.get('WifeId')
        # if not husband_id or not wife_id:   # Skip this family if it doesn't have husband or wife IDs
        #     continue # Skip to next family

        # # husb_data = getIndiById(indi_data, fam['HusbandId'])
        # # wife_data = getIndiById(indi_data, fam['WifeId'])
        # # Look for families where the husband and wife are listed as children
        # for check_fam in fam_data:
        #     children = check_fam.get('Children', [])
        #     if husband_id in children and wife_id in children:
        #         anomalies.append(f'ANOMALY: FAMILY: US18: {fam["HusbandName"]} ({husband_id}) and {fam["WifeName"]} ({wife_id}) are siblings and should not be married. Is this Alabama?')
        #         break  # Exit inner loop if anomaly found
        