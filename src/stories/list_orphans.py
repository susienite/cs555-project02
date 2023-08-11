from helper import *

def list_orphans(indi_data, fam_data):
    list = []
    for fam in fam_data:
        husb = fam['HusbandId']
        wife = fam['WifeId']
        husb_alive = getIndiById(indi_data, husb)['Alive']
        wife_alive = getIndiById(indi_data, wife)['Alive']
        num_children = len(fam['Children'])

        #Both parents are dead but have children, check every child for age
        if ((husb_alive == False) and (wife_alive == False) and (num_children > 0)) :
            for child in fam['Children']:
                child_row = getIndiById(indi_data, child)
                child_age = computeAgeDifferenceInYears(child_row['Birthday'], getToday())
                if (child_age < 18):    #less than 18, then orphan
                    string = '\t' + child_row['Name'] + " (" + str(child_age) + ") is an orphan"
                    list.append(string)
   
    if(len(list) > 0):
        heading = 'List of Orphans:' 
        list.insert(0, heading)
    return list