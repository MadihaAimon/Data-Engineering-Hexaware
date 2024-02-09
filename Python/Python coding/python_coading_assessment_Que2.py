import pandas as pd

file_path = 'new_file.csv'

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())