from helper import *

def check_marriage_before_divorce(fam_data, errors):
    for fam in fam_data:
        if (fam["Married"] == "NA" or fam["Divorced"] == "NA"):
            continue
        if (compareDates(fam["Divorced"], fam["Married"]) == -1):
            errors.append(f'ERROR: INDIVIDUAL: US04: Divorce of ({fam["Divorced"]}) of ({fam["HusbandName"]}) and ({fam["WifeName"]}) occurs before marriage date ({fam["Married"]})')
      