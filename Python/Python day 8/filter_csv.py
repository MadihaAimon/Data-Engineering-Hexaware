import pandas as pd

# Read CSV file
df = pd.read_csv('example.csv')

# Filter data based on a condition
filtered_data = df[df['Column1'] <2]

# Display filtered DataFrame
print(filtered_data)