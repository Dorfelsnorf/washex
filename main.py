from namelist import arabname, turkname
from test import namelist

import pandas as pd


def check_name(name):  # Simple check if the first name fits
    try:
        name.index(" ")
    except ValueError:
        newName = name.split(" ")
        name = newName[0]

    for nameToCheck in arabname:
        if name.lower() == nameToCheck.lower():
            return "arab"

    for nameToCheck in turkname:
        if name.lower() == nameToCheck.lower():
            return "turkish"

        return "none"


# def import_csv():               # Imports the csv file
# TODO fix this

# def wash_criteria_set():                        # Sets criteria for the wash
# TODO allow users to set their criteria and coloumn for washing


if __name__ == '__main__':

    for name in namelist:
        print(name, " ", check_name(name))
