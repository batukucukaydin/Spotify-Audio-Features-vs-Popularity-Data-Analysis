import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def standardize_columns(df):
    """
    Standardizes column names to snake_case.
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '', regex=True)
    return df

def detect_and_rename_columns(df):
    """
    Detects common variations of column names and renames them to standard ones.
    """
    # Map common variations to standard names
    column_mapping = {
        'track name': 'track_name',
        'track_title': 'track_name',
        'artist': 'artists',
        'artist_name': 'artists',
        'duration_ms': 'duration_ms',
        'duration': 'duration_ms',
        'top genre': 'genre',
        'pop': 'popularity',
        'bpm': 'tempo',
        'db': 'loudness',
        'acous': 'acousticness',
        'spch': 'speechiness',
        'dnce': 'danceability',
        'nrgy': 'energy',
        'val': 'valence',
        'live': 'liveness',
        'inst': 'instrumentalness' 
    }
    
    # Create a copy to avoid checking against modified columns immediately in a confusing way
    # though rename handles this well.
    
    # Check if we have exact matches first, if not try to map
    new_cols = {}
    for col in df.columns:
        clean_col = col.lower().strip()
        if clean_col in column_mapping:
            new_cols[col] = column_mapping[clean_col]
        # logic for 'descriptor' words
        elif 'popularity' in clean_col:
            new_cols[col] = 'popularity'
        elif 'dance' in clean_col:
            new_cols[col] = 'danceability'
        elif 'energy' in clean_col:
            new_cols[col] = 'energy'
        elif 'loud' in clean_col:
            new_cols[col] = 'loudness'
        elif 'speech' in clean_col:
            new_cols[col] = 'speechiness'
        elif 'acoust' in clean_col:
            new_cols[col] = 'acousticness'
        elif 'instrum' in clean_col:
            new_cols[col] = 'instrumentalness'
        elif 'liveness' in clean_col:
            new_cols[col] = 'liveness'
        elif 'valence' in clean_col:
            new_cols[col] = 'valence'
        elif 'tempo' in clean_col:
            new_cols[col] = 'tempo'
        elif 'duration' in clean_col:
            new_cols[col] = 'duration_ms'
            
    if new_cols:
        print(f"Renaming columns: {new_cols}")
        df = df.rename(columns=new_cols)
    
    return df, new_cols

def basic_summary(df):
    """
    Prints a basic summary of the DataFrame: head, shape, info, and missing values.
    """
    print("--- Head ---")
    print(df.head())
    print("\n--- Shape ---")
    print(df.shape)
    print("\n--- Info ---")
    print(df.info())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
def iqr_filter(df, col, k=1.5):
    """
    Filters outliers from a dataframe column using the IQR method.
    Returns the filtered dataframe and the number of rows removed.
    """
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - k * IQR
    upper_bound = Q3 + k * IQR
    
    initial_rows = len(df)
    df_filtered = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    final_rows = len(df_filtered)
    removed_rows = initial_rows - final_rows
    
    print(f"Outlier Filtering for '{col}': Removed {removed_rows} rows (Bounds: {lower_bound:.2f}, {upper_bound:.2f})")
    
    return df_filtered, removed_rows

def savefig(filename):
    """
    Saves the current matplotlib figure to the outputs directory.
    Ensures the directory exists.
    """
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    path = os.path.join(output_dir, filename)
    plt.savefig(path, bbox_inches='tight', dpi=100)
    print(f"Saved plot to {path}")
