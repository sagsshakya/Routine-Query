import os
import pandas as pd

from utils import dump_json, load_teachers

root_dir = 'data\\intermidiate'
input_filenames = os.listdir(root_dir)
input_filepaths = [os.path.join(root_dir, NAME)  for NAME in input_filenames]

keys = [item.split(".")[0][-2:] for item in input_filenames]

# Save format.
    ## key_grade : dict(routine)
df_dict = {KK: pd.read_csv(FILEPATH, delimiter = "\t").to_dict() for KK, FILEPATH in zip(keys, input_filepaths)}

# Serialize to JSON.
dump_json(df_dict)

# Update teachers - universal.
teachers_coll = set()
for dictionary in df_dict.values():
    teachers_set = load_teachers(pd.DataFrame(dictionary))
    teachers_coll = teachers_coll.union(teachers_set)

print(teachers_coll.difference({'void'}))