import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta

# Local modules.
from utils import load_teachers

root_dir = 'data'
g_11_path = os.path.join(root_dir, 'daily_routine-11.txt')
g_12_path = os.path.join(root_dir, 'daily_routine-12.txt')

df_11 = pd.read_csv(g_11_path, delimiter = "\t")
df_12 = pd.read_csv(g_12_path, delimiter = "\t")

# Teachers' list.
df_college = pd.concat([df_11, df_12]).reset_index(drop = True)
teachers_college = load_teachers(df_college)
print(teachers_college)

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

