import sys
from datetime import date, datetime
from prettytable import PrettyTable

from helper import *
from stories.birth_before_marriage import check_birth_before_marriage
from stories.marriage_after_14 import check_marriage_after_14
from stories.dates_before_current import check_dates_before_curr
from stories.list_recent_deaths_and_births import make_list_of_recent
from stories.check_parents_not_too_old import check_parents_not_too_old
from stories.check_sibling_spacing import check_sibling_spacing
from stories.marriage_before_divorce2 import check_marriage_before_divorce
from stories.check_no_bigamy import check_no_bigamy
from stories.check_less_than_15_siblings import check_less_than_15_siblings
from stories.check_at_most_pentuplets import check_at_most_pentuplets

valid_tags = {'INDI': '0', 'NAME': '1', 'SEX': '1', 'BIRT': '1', 'DEAT': '1', 'FAMC': '1', 
            'FAMS': '1', 'FAM': '0', 'HUSB': '1', 'WIFE': '1', 'CHIL': '1', 'MARR':'1' ,'DIV': '1', 
            'DATE': '2', 'HEAD': '0','TRLR': '0', 'NOTE': '0'}
ignore_tags = ['HEAD', 'TRLR', 'NOTE']
date_tags = ['BIRT', 'DEAT', 'DIV', 'MARR']

def find_stories(indi_data, fam_data):
    errors, anomalies = [], []
    # add story functions here
    # sprint1
    check_birth_before_marriage(indi_data, fam_data, errors)
    check_marriage_after_14(indi_data, fam_data, errors)
    check_dates_before_curr(indi_data, fam_data, errors)
    check_parents_not_too_old(indi_data, fam_data, anomalies)
    check_sibling_spacing(indi_data, fam_data, anomalies)

    #sprint 2 & M5.B1
    check_marriage_before_divorce(fam_data, errors)
    check_no_bigamy(fam_data, anomalies)
    check_less_than_15_siblings(fam_data, errors)
    check_at_most_pentuplets(indi_data, fam_data, errors) # collaborative driver/navigator function
    # ...
    
    return (errors, anomalies)

def make_list(indi_data, fam_data):
    all_lists = []

    #sprint 2 
    all_lists.append(make_list_of_recent(indi_data, 'Death'))
    all_lists.append(make_list_of_recent(indi_data, 'Birthday'))

    return all_lists

def extract(word):
    word = word.replace('@','')
    return word
    
def parser(filename):
    #parse GEDCOM data into list of (list of words = one line) 
    lines =[] 
    with open(filename) as fn:
        for line in fn:
            string = ''.join(line.strip())
            wordList = string.split()
            lines.append(wordList)

    #individuals and family tables 
    indi_data = []
    fam_data = [] 
    it_num = 0 
    fam_num = 0 
    typeDate = ''   #birth, death, div, marr

    #read each line and make inidividual or family record 
    for list in lines:
        if (list[1] in ignore_tags): #ignore some tags
            continue 

        if (list[0] == '0' and len(list) == 3):  
            if (list[2] == 'INDI') :    #make new individual record
                indi_row =  {'ID': extract(list[1]), 'Name': '','Gender': '', 'Birthday': '', 'Age': '',
                    'Alive': True, 'Death': 'NA', 'Child': [], 'Spouse': []}
                indi_data.append(indi_row)
                it_num += 1
            elif (list[2] == 'FAM'):        #make new fam record
                fam_row = { 'ID': extract(list[1]), 'Married': 'NA','Divorced': 'NA', 'HusbandId': '','HusbandName': '',
                    'WifeId': '','WifeName': '','Children': []}
                fam_data.append(fam_row)
                fam_num+=1
            else:
                continue
    

        #check if valid tag and tag matches number 
        if (list[1] not in valid_tags.keys()):
            continue
        elif (list[0] != valid_tags[list[1]]):
            continue
        else: 
            #VALID 
            #convert end arguments to a string
            endArgs = " ".join(list[2:])
            
            #remember type of DATE 
            if (list[1] in date_tags):
                if (list[1] == 'BIRT'): typeDate = "bir"
                if (list[1] == 'DEAT'): typeDate = "dea"
                if (list[1] == 'DIV'): typeDate = "div"
                if (list[1] == 'MARR'): typeDate = "mar"
                continue   #skip to next line

            #individual attributes 
            if (list[1] == 'NAME'): indi_data[it_num-1]['Name'] = endArgs
            if(list[1] == 'SEX'): indi_data[it_num-1]['Gender'] = endArgs
            if (list[1] == 'DATE'): 
                if (typeDate == "bir"): 
                    indi_data[it_num-1]['Birthday'] = convertArgToDate(list[2:])
                    typeDate = ''   #reset
                if (typeDate == "dea"):
                    indi_data[it_num-1]['Death'] = convertArgToDate(list[2:])
                    indi_data[it_num-1]['Alive'] = False
                    typeDate = ''
            if (list[1] == 'FAMC'): 
                    indi_data[it_num-1]['Child'].append(extract(endArgs))
            if (list[1] == 'FAMS'): 
                    indi_data[it_num-1]['Spouse'].append(extract(endArgs))
                
            #family attributes
            if(list[1] == 'HUSB'): 
                hubID = extract(endArgs)
                fam_data[fam_num-1]['HusbandId'] = hubID
                fam_data[fam_num-1]['HusbandName'] = (getIndiById(indi_data, hubID))['Name']
            if(list[1] == 'WIFE'): 
                wifID = extract(endArgs)
                fam_data[fam_num-1]['WifeId'] = wifID
                fam_data[fam_num-1]['WifeName'] = (getIndiById(indi_data, wifID))['Name']
            if(list[1] == 'CHIL'): 
                childID = extract(endArgs)
                fam_data[fam_num-1]['Children'].append(childID)
            if (list[1] == 'DATE'):
                if (typeDate == "mar"): 
                    fam_data[fam_num-1]['Married'] = str(convertArgToDate(list[2:]))
                    typeDate = ''   #reset
                if (typeDate == "div"): 
                    fam_data[fam_num-1]['Divorced'] = str(convertArgToDate(list[2:]))
                    typeDate = ''      #needs to have an error if Date doesn't follow any of the 4 
    # end of loop 

    #calculate age for the individual record and make changes for pretty-print 
    for row in indi_data:
        age = 0
        birth_object = str(row['Birthday'])
        death_object = str(row['Death'])
        if (death_object == 'NA') :
            age = computeAgeDifference(birth_object, getToday(), "overall")
        else:
            age = computeAgeDifference(birth_object, death_object, "overall")
        row['Death'] = str(death_object)
        row['Birthday'] = str(birth_object)
        row['Age'] = age

        if (row['Child'] == []):
            row['Child'] = 'None'
        if (row['Spouse'] == []):
            row['Spouse'] = 'NA'
    
    return indi_data, fam_data

def main(filename):
    indi_data, fam_data = parser(filename)

    #make pretty tables
    indi_table = PrettyTable()
    indi_table.title = 'Individuals Table'
    indi_table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    for row in indi_data:
        row_values = row.values()
        indi_table.add_row(row_values)
 
    family_table = PrettyTable()
    family_table.title= 'Families Table'
    family_table.field_names = ['ID', 'Married', 'Divorced', 'HusbandId', 'HusbandName', 'WifeId', 'WifeName', 'Children']
    for row in fam_data:
        row_values = row.values()
        family_table.add_row(row_values)

    #all errors or anomolies
    errors, anomalies = find_stories(indi_data, fam_data)

    #lists 
    all_lists = make_list(indi_data, fam_data)
    
    printOutput(indi_table, family_table, errors, anomalies, all_lists)
    # writeToOutput(indi_table, family_table, recent_deaths_table, errors, anomalies, all_lists)


if __name__ == "__main__":
    file = sys.argv[1]
    main(file)

