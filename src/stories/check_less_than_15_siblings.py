from helper import *

def check_less_than_15_siblings(fam_data, anomalies):
    for fam in fam_data:
        if (len(fam['Children']) > 15):
            anomalies.append(f'ANOMALY: FAMILY: US15: {fam["HusbandName"]} and {fam["WifeName"]} of {fam["ID"]} have more than 15 children (that are siblings)!')
