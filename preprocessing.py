import pandas as pd

def clean_data(df):
    df = df.copy()
    df.dropna(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def add_features(df):
    df["Month"] = df["Date"].dt.month
    return df