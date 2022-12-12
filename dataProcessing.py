import pandas as pd


def temporal_data_process(file):
    df = pd.read_csv(file.name, encoding='utf-8')
    df = df.replace("\'", "\\'", regex=True)
    return df