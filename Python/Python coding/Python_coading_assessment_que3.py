import pandas as pd

file_path = 'new_file.csv'

df = pd.read_csv(file_path)

# Read CSV file into a DataFrame
data_frame   = pd.DataFrame(df)

print(data_frame)