from helper import *

def list_living_single(indi_data):
    list = []
    for person in indi_data:
        if (person['Alive'] == True and person['Spouse'] == 'NA'):
            string = "\t" + person['Name'] + " is alive and single"
            list.append(string)
    if(len(list) > 0):
        heading = 'List of Alive and Single Individuals:' 
        list.insert(0, heading)
    return list