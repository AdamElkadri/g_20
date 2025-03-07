import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = r"/Users/adam/Desktop/G_20/G_20_Data_CN.csv"

df = pd.read_csv(file_path, encoding="latin1")
print("Initial data:")
print(df.head())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.replace(",", "", regex=True)
    df[col] = pd.to_numeric(df[col], errors='ignore')

print("\nDF Cleaned Data:")
print(df.head())

english_speakers = ["Australia", "Canada", "United Kingdom", "United States"]
df["English Speaker"] = df["Country"].isin(english_speakers)
print("\nData with English_Speaker column added:")
print(df.head(22))

print("\nDescriptive Statistics")
print(df.describe())

plt.figure(figsize=(8,6))
sns.histplot(df["Nom_GDP_Per_capita"].dropna(), bins=10, kde=True, color="skyblue", edgecolor="black")
plt.title("Distribution of Nominal GDP per Capita")
plt.xlabel("Nominal GDP per Capita")
plt.ylabel("Frequency")
plt.show(block=False)

plt.figure(figsize=(8,6))
sns.boxplot(x="English Speaker", y="Nom_GDP_Per_capita", data=df)
plt.title("Nominal GDP per Capita by English Speaker Status")
plt.xlabel("English Speaker (True/False)")
plt.ylabel("Nominal GDP per Capita")
plt.show()

corr_coef = np.corrcoef(df["English Speaker"], df["Nom_GDP_Per_capita"])[0,1]
print("CORRELATION", corr_coef)

group_summary = df.groupby("English Speaker")["Nom_GDP_Per_capita"].mean()
print("\nAverage Nominal GDP per Capita by English Speaker status:")
print(group_summary)

