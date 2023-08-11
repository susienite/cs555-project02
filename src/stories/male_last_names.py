def check_male_last_names(fam_data, anomalies):
    for fam in fam_data:
        husband_name = fam['HusbandName']
        husband_last_name = husband_name.split()[-1]  #assuming the last name is the last word in 'HusbandName'
        for child in fam['Children']:
            if child['Gender'] == 'M':
                child_last_name = child['ChildName'].split()[-1]
                if child_last_name != husband_last_name:
                    anomalies.append(f'ANOMALY: FAMILY: US13: {child["ChildName"]} ({child["ChildId"]}) does not have the same last name as his father {husband_name} ({fam["HusbandId"]})')
