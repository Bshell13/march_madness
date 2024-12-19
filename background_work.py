import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
# Import a file to extract data from API

# Load Data sets into DataFrame

# Show shape of dataset
print(df.shape)

# Show data types for each column
print(df.dtypes)

# Inspect basics stats for numerical columns
print(df.describe()

# Detect Null Values
if df.isnull().values.isany() == False:
  print('There are zero NULL values in the dataset.')
else:
  print(f'There are {df.isnull().sum)} NULL values in the dataset.')

# Inspect value counts for categorical columns
for col in df.select_dtypes(include=['object', 'category']).columns:
  sns.countplot(x=col, data=df)

# If you want to rename columns, do so here
# df.rename(columns{'original name: new name, ...}, inplace=True)

# Display histograms of numerical columns
df.hist()

# Determining the correlation between columns using a correlation matrix
df.corr()
# Use scatterplots to better understand correlation
