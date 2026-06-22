import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())
print("Shape of dataset:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())
print("\nGender Count:")
print(df['Sex'].value_counts())

print("\nSurvival Count:")
print(df['Survived'].value_counts())

print("\nPassenger Class Count:")
print(df['Pclass'].value_counts())

print("\nAverage Age:")
print(df['Age'].mean())

print("\nMaximum Age:")
print(df['Age'].max())

print("\nMinimum Age:")
print(df['Age'].min())

print("\nAverage Fare:")
print(df['Fare'].mean())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nUnique Values in Each Column:")
print(df.nunique())
print("\nMedian Age:")
print(df['Age'].median())

print("\nMost Frequent Age (Mode):")
print(df['Age'].mode())

print("\nUnique Embarked Locations:")
print(df['Embarked'].unique())