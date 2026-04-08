import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\AL-ML\Day4_Tasks\data\data.csv")

# REMOVE EXTRA SPACES FROM COLUMN NAMES
df.columns = df.columns.str.strip()

# 1. Identify missing values
print("Missing Values:\n", df.isnull().sum())

# 2. Fill missing Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. Fill missing Score with 0
df['Score'] = df['Score'].fillna(0)

print("\nCleaned Data:\n", df)