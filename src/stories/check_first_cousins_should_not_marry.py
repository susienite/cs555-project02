from helper import *

def check_first_cousins_should_not_marry(fam_data, anomalies):

    # Get a mapping of parents to their children
    children_of_parents = {}
    for fam in fam_data:
        children_of_parents[(fam.get('HusbandId'), fam.get('WifeId'))] = fam.get('Children', [])

    # Check if any married couples are first cousins
    for (parents1, children1) in children_of_parents.items():
        for (parents2, children2) in children_of_parents.items():
            if parents1 != parents2:  # Ensure we're not comparing the same family
                for child1 in children1:
                    for child2 in children2:
                        if are_married(child1, child2, fam_data):
                            anomalies.append(f'ANOMALY: FAMILY: US19: {get_name(child1, fam_data)} ({child1}) and {get_name(child2, fam_data)} ({child2}) are first cousins and should not be married.')

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
