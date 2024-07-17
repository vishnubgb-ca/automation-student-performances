import pandas as pd
import numpy as np

# Load data from csv file
df = pd.read_csv('data.csv')

# Delete rows with NaN values in 'lead_time' column
df = df.dropna(subset=['lead_time'])

# Delete duplicate rows
df = df.drop_duplicates()

# Delete 'sku' column
df = df.drop(['sku'], axis=1)

# Save the cleaned data frame to a new csv file
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head(5))