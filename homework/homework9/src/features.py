import pandas as pd
import numpy as np

def create_features(df):
    df['spend_income_ratio'] = df['monthly_spend'] / df['income']
    df['credit_limit'] = df['income'] * df['credit_score']
    region_freq = df['region'].value_counts(normalize=True)
    df['region_freq'] = df['region'].map(region_freq)
    print(df)
    return df