import os
import pandas as pd

from utils import dump_json

root_dir = 'data\\intermidiate'
input_filenames = os.listdir(root_dir)
input_filepaths = [os.path.join(root_dir, NAME)  for NAME in input_filenames]

keys = [item.split(".")[0][-2:] for item in input_filenames]

# Save format.
    ## key_grade : dict(routine)
df_dict = {KK: pd.read_csv(FILEPATH, delimiter = "\t").to_dict() for KK, FILEPATH in zip(keys, input_filepaths)}

dump_json(df_dict)
