from helper import *

def check_no_bigamy(indi_data, fam_data, anomalies):
    married = {}
    for fam in fam_data:
        # and Divorced is not NA
        # if husband not in keys... 
            # if not divorced then add key.
            # if divorced don't add key. 
        # if husband in keys and if not divorced then add anomaly.
        # if husband in keys and if divorced ignore. 
        if(fam['HusbandId'] not in married.keys()):
            if(fam['Divorced'] == 'NA'):
                married.update({fam['HusbandId']: fam['ID']})
        else:
            if(fam['Divorced'] == 'NA'):
                anomalies.append(f'ANOMALY: FAMILY: US11: {fam["HusbandName"]} ({fam["HusbandId"]}) has a bigamous marriage')

        if(fam['WifeId'] not in married.keys()):
            if(fam['Divorced'] == 'NA'):
                married.update({fam['WifeId']: fam['ID']})
        else:
            if(fam['Divorced'] == 'NA'):
                anomalies.append(f'ANOMALY: FAMILY: US11: {fam["WifeName"]} ({fam["WifeId"]}) has a bigamous marriage')
