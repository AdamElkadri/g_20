import pandas as pd
file_path = r"/Users/adam/Desktop/G_20/G_20_Data_CN.csv"

df = pd.read_csv(file_path, encoding="latin1")
print("Initial data:")
print(df.head())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.replace(",", "", regex=True)
    df[col] = pd.to_numeric(df[col], errors='ignore')

print("\nDF Cleaned Data:")
print(df.head())




