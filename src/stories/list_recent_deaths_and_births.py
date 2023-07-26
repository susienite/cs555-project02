from helper import *

# return a list of recent deaths or births 
# arg = deaths or births 
def make_list_of_recent(indi_data, arg):
    list = []
    argString = ""
    if (arg == "Birthday"):
        argString = "Birth"
    else:
        argString = arg
        
    for person in indi_data:
        d1 = person[arg]
        if (d1 == None or d1 == 'NA'):
            continue
        elif (datesWithinLimit(d1, getToday(), 30, 'days')):
            string = "\t" + person['Name'] + "'s " + argString + " is " + d1
            list.append(string)
    
    if(len(list) > 0): # to avoid printing heading if no recent deaths or births
        heading = 'List of Recent ' + argString + 's' + ' (within last 30 days):' 
        list.insert(0, heading)

    return list

  




