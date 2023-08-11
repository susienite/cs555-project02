from helper import *

def check_siblings_should_not_marry(fam_data, anomalies):
    
    # Check if any married couples are siblings
    for fam in fam_data:
        husband_id = fam['HusbandId']
        wife_id = fam['WifeId']

        # Look for families where the husband and wife are listed as children
        for check_fam in fam_data:
            children = check_fam.get('Children', [])
            if husband_id in children and wife_id in children:
                anomalies.append(f'ANOMALY: FAMILY: US18: {fam["HusbandName"]} ({husband_id}) and {fam["WifeName"]} ({wife_id}) are siblings and should not be married. Is this Alabama?')
                break  # Exit inner loop if anomaly found


# from helper import *

# def check_no_bigamy(fam_data, anomalies):
#     married = {}
#     for fam in fam_data:
#         if(fam['HusbandId'] not in married.keys() and fam['Divorced'] == 'NA'):
#             married.update({fam['HusbandId']: fam['ID']})
#         elif(fam['Divorced'] == 'NA'):
#             anomalies.append(f'ANOMALY: FAMILY: US11: {fam["HusbandName"]} ({fam["HusbandId"]}) has a bigamous marriage')

#         if(fam['WifeId'] not in married.keys() and fam['Divorced'] == 'NA'):
#             married.update({fam['WifeId']: fam['ID']})
#         elif(fam['Divorced'] == 'NA'):
#             anomalies.append(f'ANOMALY: FAMILY: US11: {fam["WifeName"]} ({fam["WifeId"]}) has a bigamous marriage')