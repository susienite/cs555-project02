from datetime import date, datetime, timedelta

months_conv = {  'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
            'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC':12}


#Return today's date in string 
def getToday():
    return str(date.today())

#Convert argument 12 JAN 1990 into datetime.date
def convertArgToDate(arg):
    day = int(arg[0])
    month = months_conv[arg[1]]
    year = int(arg[2])
    return date(year, month,day)

def computeAgeFromDeath(birth, death):
    age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))
    return age

#Get record for individual ID 
def getIndiById(table, id):    
    for row in table:
        if (row['ID'] == id): return row
    
# 1 if date1 is later than date2, -1 if date1 is earlier than date2, 0 if equal
def compareDates(date1, date2):
    d1 = date1.split('-')
    d1y, d1m, d1d = (int(d1[0]), int(d1[1]), int(d1[2]))
    d2 = date2.split('-')
    d2y, d2m, d2d = (int(d2[0]), int(d2[1]), int(d2[2]))
    
    if(d1y > d2y): return 1
    if(d1y < d2y): return -1
    if(d1m > d2m): return 1
    if(d1m < d2m): return -1
    if(d1d > d2d): return 1
    if(d1d < d2d): return -1
    return 0


#return True if date1 and date2 are within limit units, otherwise return False
#limit is a number
#units is a string ('days', 'months', 'years')
#TAKEN FROM LECTURE MATERIAL
def datesWithinLimit(date1, date2, limit, units):
    conversion = {'days': 1, 'months': 30.4, 'years': 365.25}
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    diff = abs((d2 - d1).days)/ conversion[units]
    return diff <= limit 

#Compute the difference between two dates given unit
#units is a string ('overall')
def computeAgeDifference(start, end, units):
    d1 = datetime.strptime(start, '%Y-%m-%d')
    d2 = datetime.strptime(end, '%Y-%m-%d')
    if (units == "overall"):
        return d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day))
    else:
        return 

#Compute the difference between two dates in terms of months
def computeAgeDifferenceInMonths(date1, date2):    
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return (d2.year - d1.year) * 12 + d2.month - d1.month

#Compute the difference between two dates in terms of days
def computeAgeDifferenceInDays(date1, date2):
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return (d2 - d1).days

#Write to output file 
def writeToOutput(indi_table, family_table, recent_deaths_table, errors, anomalies, all_lists):
    with open('output.txt', 'w') as f:
        itable = str(indi_table) + '\n'
        ftable = str(family_table) + '\n'
        deathstable = str(recent_deaths_table) + '\n'
        f.write(itable)
        f.write(ftable)
        f.write(deathstable)
        #... for future sprints

        for e in errors:
            err = e + '\n'
            f.write(err)
        for a in anomalies:
            an = a + '\n'
            f.write(an)
        for list in all_lists:
            for line in list:
                li = line + '\n'
                f.write(li)
        
        f.flush()
        f.close()

#Print the output in console        
def printOutput(indi_table, family_table, errors, anomalies, all_lists):
    print(indi_table)
    print(family_table) 
    for error in errors:
        print(error)
    for anomaly in anomalies:
        print(anomaly) 
    for list in all_lists:
        for line in list:
            print(line)