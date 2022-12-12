import pandas as pd


def temporal_data_process(file):
    df = pd.read_csv(file, encoding='utf-8')
    return df