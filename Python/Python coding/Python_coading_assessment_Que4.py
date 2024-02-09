import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Using query to filter data (e.g., selecting individuals older than 30)
filtered_df = df.query('Age > 30')

# Display the filtered DataFrame
print("\nFiltered DataFrame:")
print(filtered_df)