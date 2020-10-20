import pandas as pd
import os
import json
import ast


CURATIONS_DIR = os.path.join('data', 'annotations')

def load_curations(curations_dir = CURATIONS_DIR) -> pd.DataFrame:
    curations = []
    for file_name in os.listdir(curations_dir):
        path = os.path.join(curations_dir, file_name)
        with open(path, 'r') as f:
            curations.append(json.load(f))
    
    df = pd.DataFrame(curations)
    return df


def get_annotation_spans(curations: pd.DataFrame = None) -> pd.DataFrame:
    index = []
    spans_column = 'crowd-entity-annotation.entities'
    columns = ['dataObject', 'workerId', 'startOffset', 'endOffset', 'label']
    data = {col:[] for col in columns}
    
    for i, row in curations.iterrows():
        span_list = ast.literal_eval(row[spans_column])
        for span in span_list:
            index.append(i)
            data[columns[0]].append(row[columns[0]])
            data[columns[1]].append(row[columns[1]])
            for k, v in span.items():
                data[k].append(v)
    
    df = pd.DataFrame(data, index=index)
    
    return df