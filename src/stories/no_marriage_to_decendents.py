def build_descendants_dict(fam_data):
    descendants = {}
    for fam in fam_data:
        if fam['HusbandId'] not in descendants:
            descendants[fam['HusbandId']] = []
        if fam['WifeId'] not in descendants:
            descendants[fam['WifeId']] = []
        descendants[fam['HusbandId']].extend(fam['Children'])
        descendants[fam['WifeId']].extend(fam['Children'])
    return descendants

def propagate_descendants(descendants):
    change = True
    while change:
        change = False
        for parent, direct_children in descendants.items():
            indirect_children = set()
            for child in direct_children:
                if child in descendants:
                    indirect_children.update(descendants[child])
            new_descendants = direct_children.union(indirect_children)
            if len(new_descendants) > len(direct_children):
                descendants[parent] = new_descendants
                change = True

def check_no_marriages_to_descendants(fam_data, anomalies):
    descendants = build_descendants_dict(fam_data)
    propagate_descendants(descendants)
    for fam in fam_data:
        if fam['HusbandId'] in descendants[fam['WifeId']]:
            anomalies.append(f'ANOMALY: FAMILY: US12: {fam["WifeName"]} ({fam["WifeId"]}) is married to a descendant {fam["HusbandName"]} ({fam["HusbandId"]})')
        if fam['WifeId'] in descendants[fam['HusbandId']]:
            anomalies.append(f'ANOMALY: FAMILY: US12: {fam["HusbandName"]} ({fam["HusbandId"]}) is married to a descendant {fam["WifeName"]} ({fam["WifeId"]})')
