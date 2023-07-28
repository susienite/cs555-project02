from helper import *

def list_large_age_diff(indi_data, fam_data):
    list = []
    for family in fam_data:
        husb = family['HusbandId']
        wife = family['WifeId']
        marr_date = family['Married']

        husb_row = getIndiById(indi_data, husb)
        wife_row = getIndiById(indi_data, wife)
        husb_birth = husb_row['Birthday']
        wife_birth = wife_row['Birthday']
        
        if (husb_birth != 'NA' and wife_birth != 'NA' and marr_date != 'NA'):
            #Compute age at marriage. Assume they were alive during marriage.
            husb_age = computeAgeDifference(husb_birth, marr_date , "overall")
            wife_age = computeAgeDifference(wife_birth, marr_date, "overall")  

            #Append to list if age of one spouse is more than 2x the other at marriage
            if ((husb_age/wife_age) > 2):
                diff = str(round(husb_age/wife_age, 1))
                strHA = str(husb_age)
                strWA = str(wife_age)
                string = "\t" + husb_row['Name'] + " at age " + strHA + " married " + wife_row['Name'] + " at age " + strWA + " which is a " + diff + " times difference"
                list.append(string)
            if ((wife_age/husb_age) > 2):
                diff = str(round(wife_age/husb_age, 1))
                strHA = str(husb_age)
                strWA = str(wife_age)
                string = "\t" + wife_row['Name'] + " at age " + strWA + " married " + husb_row['Name'] + " at age " + strHA + " which is " + diff + " times difference"
                list.append(string) 
    if(len(list) > 0): # to avoid printing heading if no recent deaths or births
        heading = 'List of Large Age Differences' 
        list.insert(0, heading)   
    return list