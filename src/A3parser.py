import sys
from datetime import date, datetime
from prettytable import PrettyTable

from helper import *
from stories.birth_before_marriage import check_birth_before_marriage
from stories.marriage_after_14 import check_marriage_after_14

valid_tags = {'INDI': '0', 'NAME': '1', 'SEX': '1', 'BIRT': '1', 'DEAT': '1', 'FAMC': '1', 
            'FAMS': '1', 'FAM': '0', 'HUSB': '1', 'WIFE': '1', 'CHIL': '1', 'MARR':'1' ,'DIV': '1', 
            'DATE': '2', 'HEAD': '0','TRLR': '0', 'NOTE': '0'}
ignore_tags = ['HEAD', 'TRLR', 'NOTE']
date_tags = ['BIRT', 'DEAT', 'DIV', 'MARR']
months_conv = {  'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
            'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC':12}

def find_stories(indi_data, fam_data):
    errors, anomalies = [], []
    # add story functions here
    check_birth_before_marriage(indi_data, fam_data, errors)
    check_marriage_after_14(indi_data, fam_data, errors)
    # ...
    
    return (errors, anomalies)


def extract(word):
    word = word.replace('@','')
    return word

def convertDate(arg):
    day = int(arg[0])
    month = months_conv[arg[1]]
    year = int(arg[2])
    return date(year, month,day)
    
    
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
    
        
        #valid tag and number?
        if (list[1] not in valid_tags.keys()):
            continue
        elif (list[0] != valid_tags[list[1]]):
            continue
        else: #yes
            endArgs = " ".join(list[2:])
            
            #Dates are weird
            if (list[1] in date_tags):
                if (list[1] == 'BIRT'): typeDate = "bir"
                if (list[1] == 'DEAT'): typeDate = "dea"
                if (list[1] == 'DIV'): typeDate = "div"
                if (list[1] == 'MARR'): typeDate = "mar"
                continue

            #individual attributes 
            if (list[1] == 'NAME'): indi_data[it_num-1]['Name'] = endArgs
            if(list[1] == 'SEX'): indi_data[it_num-1]['Gender'] = endArgs
            if (list[1] == 'DATE'): 
                if (typeDate == "bir"): 
                    indi_data[it_num-1]['Birthday'] = convertDate(list[2:])
                    typeDate = ''   #reset
                if (typeDate == "dea"):
                    indi_data[it_num-1]['Death'] = convertDate(list[2:])
                    indi_data[it_num-1]['Alive'] = False
                    typeDate = ''
            if (list[1] == 'FAMC'): 
                indi_data[it_num-1]['Child'].append(extract(endArgs))
            if (list[1] == 'FAMS'): 
                indi_data[it_num-1]['Spouse'].append(extract(endArgs))
            
            #family attributes
            if(list[1] == 'HUSB'): 
                hub = extract(endArgs)
                fam_data[fam_num-1]['HusbandId'] = hub
                fam_data[fam_num-1]['HusbandName'] = getSpouseName(indi_data, hub)
            if(list[1] == 'WIFE'): 
                wif = extract(endArgs)
                fam_data[fam_num-1]['WifeId'] = wif
                fam_data[fam_num-1]['WifeName'] = getSpouseName(indi_data, wif)
            if(list[1] == 'CHIL'): 
                child_extracted = extract(endArgs)
                fam_data[fam_num-1]['Children'].append(child_extracted)
            if (list[1] == 'DATE'):
                if (typeDate == "mar"): 
                    fam_data[fam_num-1]['Married'] = str(convertDate(list[2:]))
                    typeDate = ''   #reset
                if (typeDate == "div"): 
                    fam_data[fam_num-1]['Divorced'] = str(convertDate(list[2:]))
                    typeDate = ''      #needs to have an error if Date doesn't follow any of the 4 
    
    #calculate age
    for row in indi_data:
        age = 0
        birth_object = row['Birthday']
        death_object = row['Death']
        if (death_object == 'NA') :
            age = computeAgeFromToday(birth_object)
        else:
            age = computeAgeFromDeath(birth_object, death_object)
            row['Death'] = str(death_object)
        row['Birthday'] = str(birth_object)
        row['Age'] = age
    
    return indi_data, fam_data

def main(filename):
    indi_data, fam_data = parser(filename)
    
    # stories
    errors, anomalies = find_stories(indi_data, fam_data)
    for error in errors:
        print(error)
    for anomaly in anomalies:
        print(anomaly) 

    indi_table = PrettyTable()
    indi_table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']
    for row in indi_data:
        row_values = row.values()
        indi_table.add_row(row_values)
    print(indi_table)
 
    family_table = PrettyTable()
    family_table.field_names = ['ID', 'Married','Divorced', 'HusbandId','HusbandName','WifeId','WifeName','Children']
    for row in fam_data:
        row_values = row.values()
        family_table.add_row(row_values)
    print(family_table) 

if __name__ == "__main__":
    file = sys.argv[1]
    main(file)
