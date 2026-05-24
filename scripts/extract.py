import pandas as pd

def extract():
    df = pd.read_csv('data/raw/superstore.csv')

    print(df.isnull().sum())
    return df