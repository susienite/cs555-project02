from helper import *

def check_less_than_150(indi_data, errors):
    for indi in indi_data:
        if indi["Death"] == "NA": continue
        if computeAgeDifferenceInYears(indi["Birthday"], indi["Death"]) > 150:
            errors.append("ERROR: INDIVIDUAL: US07: " + indi["Name"] + ": died past 150 years old. Birth date " + indi["Birthday"] + ", Death date " + indi["Death"])