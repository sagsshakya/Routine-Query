# Necessary imports.
import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta

# Local modules.
from utils import load_teachers

# Information.
info_1 = '\n\nYou can use shortcuts like "today", "now", "tomorrow" and "yesterday".\nYou can also use date in the form DD/MM/YYYY.'
info_2 = '\nIf there are more than one, please separate the names using a comma.'

# Get day.
query = input(f"Which date or day you want to access? {info_1}\n: ")

if query not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    if query == "today" or query == "now":
        day = datetime.today().strftime("%A")
    elif query == "tomorrow":
        day = (datetime.today() + timedelta(days = 1)).strftime("%A")
    elif query == "yesterday":
        day = (datetime.today() - timedelta(days = 1)).strftime("%A")
    else:
        try:
            datetime_object = datetime.strptime(query, '%d/%m/%Y')
            day = datetime_object.strftime("%A")
        except:
            print("Incorrect input format. \nTry again!")
    print(day)

# Get name of the absentee.
absentee_list = input(f"Name the absentee(s); {info_2}\n: ").lower()
absentee_list = [name.strip() for name in absentee_list.split(",")]

print(absentee_list)    

