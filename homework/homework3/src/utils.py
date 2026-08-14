import pandas as pd
import numpy as np
from datetime import datetime

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=[np.number])
    
    if numeric_cols.empty:
        print("Warning: No numeric columns found in DataFrame.")
        return pd.DataFrame()
    
    return numeric_cols.describe()