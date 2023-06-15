from datetime import date

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
    