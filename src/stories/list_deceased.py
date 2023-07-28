from helper import *

def list_deceased(indi_data):
    list = []
    for person in indi_data:
        if (person['Alive'] == False):
            string = "\t" + person['Name'] + " is deceased"
            list.append(string)
    if(len(list) > 0):
        heading = 'List of Deceased Individuals:' 
        list.insert(0, heading)
    return list