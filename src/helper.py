from datetime import date, datetime, timedelta

months_conv = {  'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
            'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC':12}

def getToday():
    return str(date.today())

def convertDate(arg):
    day = int(arg[0])
    month = months_conv[arg[1]]
    year = int(arg[2])
    return date(year, month,day)

def computeAgeFromToday(birth):
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

def computeAgeFromDeath(birth, death):
    age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))
    return age

def getSpouseName(table, id):
    for row in table:
        if (row['ID'] == id): return row['Name']

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

def days_before_today(days):
    return date.today()-timedelta(days)

def betweenTodayAndNum(inputDate, numOfDays):
    date_obj = datetime.strptime(inputDate, '%Y-%m-%d').date()
    if (days_before_today(numOfDays) <= date_obj <= date.today() ):
        return True
    else: return False 


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

def writeToOutput(indi_table, family_table, recent_deaths_table, errors, anomalies):
    #write to output file
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
        
        f.flush()
        f.close()
        
def printOutput(indi_table, family_table, errors, anomalies):
    for error in errors:
        print(error)
    for anomaly in anomalies:
        print(anomaly) 
    print(indi_table)
    print(family_table) 