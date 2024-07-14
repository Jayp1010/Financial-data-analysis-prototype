import pandas as pd

def validate_data(df):
    if df.isnull().sum().sum() > 0:
        raise ValueError("Data contains null values")
    if (df.dtypes != 'float').sum() > 0:
        raise ValueError("Data types are incorrect")
    return True
