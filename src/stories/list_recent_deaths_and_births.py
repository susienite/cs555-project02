from helper import *
from prettytable import PrettyTable

# return a list of recent deaths or births 
# arg = deaths or births 
def make_list_of_recent(indi_data, arg):
    list = []
    heading = 'List of Recent ' + arg + 's' + ' (within last 30 days):' 
    list.append(heading)

    for person in indi_data:
        d1 = person[arg]
        if (d1 == None or d1 == 'NA'):
            continue
        elif (datesWithinLimit(d1, getToday(), 30, 'days')):
            string = "\t" + person['Name'] + "'s " + arg + " is " + d1
            list.append(string)
    return list

  




