from helper import *
from prettytable import PrettyTable

def make_list_of_recent_deaths(indi_data):
    table = PrettyTable()
    list = []
    table.title = 'List of Recent Death (within last 30 days)'

    table.field_names = ['ID', 'Name', 'Death']
    for person in indi_data:
        death_date = person['Death']
        if (death_date == None or death_date == 'NA'):
            continue
        elif (betweenTodayAndNum(death_date, 30)):
            table.add_row([person['ID'], person['Name'], death_date])
            list.append([person['ID'], person['Name'], death_date])
    print(table)
  




