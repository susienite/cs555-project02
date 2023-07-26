from helper import *

def check_no_bigamy(fam_data, anomalies):
    married = {}
    for fam in fam_data:
        if(fam['HusbandId'] not in married.keys() and fam['Divorced'] == 'NA'):
            married.update({fam['HusbandId']: fam['ID']})
        elif(fam['Divorced'] == 'NA'):
            anomalies.append(f'ANOMALY: FAMILY: US11: {fam["HusbandName"]} ({fam["HusbandId"]}) has a bigamous marriage')

        if(fam['WifeId'] not in married.keys() and fam['Divorced'] == 'NA'):
            married.update({fam['WifeId']: fam['ID']})
        elif(fam['Divorced'] == 'NA'):
            anomalies.append(f'ANOMALY: FAMILY: US11: {fam["WifeName"]} ({fam["WifeId"]}) has a bigamous marriage')