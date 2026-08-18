from sklearn.preprocessing import MinMaxScaler
def fill_missing_median(df, column_name):
    df1=df.copy()
    for col in column_name:
        if df1[col].dtype == 'float64':
            median_value = df1[col].median()
            df1[col] = df1[col].fillna(median_value)
    return df1

def drop_missing(df, threshold):
    df1=df.copy()
    l=len(df1.columns)
    return df1.dropna(thresh=int(l*threshold))

def normalize_data(df, column_name):
    df1=df.copy()
    for col in column_name:
        if df1[col].dtype == 'float64':
            scalar = MinMaxScaler()
            df1[col] = scalar.fit_transform(df1[[col]])
    return df1