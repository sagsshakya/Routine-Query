from itertools import chain
import json
import pandas as pd
import numpy as np

def load_teachers(dataframe: pd.DataFrame) -> set:
    
    # Teachers' list.
    teachers = dataframe.iloc[:, 1:].values.ravel()
    teachers = np.unique(teachers)
    teachers = [name.split("/") for name in teachers]
    teachers = set(chain.from_iterable(teachers))  
    return teachers  
    
def dump_json(df_dict: dict):
    class JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if hasattr(obj, 'to_json'):
                return obj.to_json(orient='records')
            return json.JSONEncoder.default(self, obj)    

    with open('result.json', 'w') as fp:
        json.dump(df_dict, fp, cls=JSONEncoder)