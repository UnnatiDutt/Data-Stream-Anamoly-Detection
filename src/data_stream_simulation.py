import numpy as np
import pandas as pd

def data_stream_simulation(file_path, size=1500):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Ensure the size does not exceed the length of the data
        size = min(size, len(df))
        #print(len(df))
        # Extract the relevant column (assuming the column name is 'cpu_utilization')
        data = df['value'].values[:size]
        
        return data
    except Exception as e:
        print(f"Error in data stream simulation: {e}")
        return np.array([])
