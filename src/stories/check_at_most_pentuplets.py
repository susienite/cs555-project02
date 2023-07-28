from helper import *

def check_at_most_pentuplets(indi_data, fam_data, anomalies):
    for fam in fam_data:
        if (len(fam['Children']) > 5):
            child_birthdays = {}
            for child in fam['Children']:
                birthday = findByValue(indi_data, 'ID', child)['Birthday']
                if(birthday not in child_birthdays):
                    child_birthdays[birthday] = 1
                else:
                    child_birthdays[birthday] += 1
            for birthday in child_birthdays:
                if(child_birthdays[birthday] > 5):
                    anomalies.append(f'ANOMALY: FAMILY: US15: {fam["HusbandName"]} and {fam["WifeName"]} of {fam["ID"]} has more than 5 children (that are siblings) born on {birthday}')