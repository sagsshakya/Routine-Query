import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta

# Local modules.
from utils import load_teachers

# Get day.
query = input("Which date or day you want to access? : ")
if query not in ("Monday","Tuesday","Wednesday","Thursday","Friday"):
    if query == "today":
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
absentee_list = input("Name the absentee(s); if there are more than one, please separate the names using a comma : ")
absentee_list = absentee_list.split(",")

print(absentee_list)    

