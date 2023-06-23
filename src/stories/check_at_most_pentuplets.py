from helper import *

def check_at_most_pentuplets(fam_data, anomalies):
    for fam in fam_data:
        if (fam['Children'].length > 5):
            child_birthdays = {}
            for child in fam['Children']:
                if(child_birthdays[child['Birthday']] == None):
                    child_birthdays[child['Birthday']] = 1
                else:
                    child_birthdays[child['Birthday']] += 1
            for birthday in child_birthdays:
                if(child_birthdays[birthday] > 15):
                    anomalies.append(f'ANOMALY: FAMILY: US15: {fam["HusbandName"]} and {fam["WifeName"]} of {fam["ID"]} has more than 5 children (that are siblings) born on {birthday}')