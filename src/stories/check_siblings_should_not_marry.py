from helper import *

def check_siblings_should_not_marry(fam_data, anomalies):
    
    married_individuals = set()
    for fam in fam_data:
        married_individuals.add(fam.get('HusbandId'))
        married_individuals.add(fam.get('WifeId'))

    # Check if any married couples are siblings
    for fam in fam_data:
        children = fam.get('Children', [])
        married_siblings = [child for child in children if child in married_individuals]
        
        for i in range(len(married_siblings)):
            for j in range(i+1, len(married_siblings)):
                if are_married(married_siblings[i], married_siblings[j], fam_data):
                    anomalies.append(f'ANOMALY: FAMILY: US18: {get_name(married_siblings[i], fam_data)} ({married_siblings[i]}) and {get_name(married_siblings[j], fam_data)} ({married_siblings[j]}) are siblings and should not be married. Is this Alabama?')

def are_married(individual1, individual2, fam_data):
    for fam in fam_data:
        if (fam.get('HusbandId') == individual1 and fam.get('WifeId') == individual2) or (fam.get('HusbandId') == individual2 and fam.get('WifeId') == individual1):
            return True
    return False

def get_name(individual_id, fam_data):
    for fam in fam_data:
        if fam.get('HusbandId') == individual_id:
            return fam.get('HusbandName')
        if fam.get('WifeId') == individual_id:
            return fam.get('WifeName')
    return None


# def check_siblings_should_not_marry(fam_data, anomalies):
    
#     # Check if any married couples are siblings
#     for fam in fam_data:
#         husband_id = fam.get('HusbandId')
#         wife_id = fam.get('WifeId')
#         children = fam.get('Children', [])
#         if husband_id in children and wife_id in children:
#                 anomalies.append(f'ANOMALY: FAMILY: US18: {fam["HusbandName"]} ({husband_id}) and {fam["WifeName"]} ({wife_id}) are siblings and should not be married. Is this Alabama?')
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
        