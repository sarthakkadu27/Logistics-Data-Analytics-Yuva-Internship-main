# Week 2 - Data Collection, Cleaning and Preprocessing
# Yuva Intern - Logistics Data Analytics

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. Load the raw logistics dataset
# ---------------------------------------------------------

df = pd.read_csv("logistics_raw_data.csv")

print("RAW DATASET")
print("=" * 50)
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

# ---------------------------------------------------------
# 2. Check missing values
# ---------------------------------------------------------

print("\nMISSING VALUES BEFORE CLEANING")
print("=" * 50)
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. Check duplicate records
# ---------------------------------------------------------

print("\nDUPLICATE RECORDS")
print("=" * 50)
print("Number of duplicates:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# ---------------------------------------------------------
# 4. Convert date column
# ---------------------------------------------------------

if "Shipment_Date" in df.columns:
    df["Shipment_Date"] = pd.to_datetime(
        df["Shipment_Date"],
        errors="coerce"
    )

# ---------------------------------------------------------
# 5. Standardize categorical columns
# ---------------------------------------------------------

categorical_columns = [
    "Origin",
    "Destination",
    "Vehicle_Type",
    "Delivery_Status"
]

for column in categorical_columns:
    if column in df.columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )

# ---------------------------------------------------------
# 6. Handle missing numerical values
# ---------------------------------------------------------

numerical_columns = [
    "Distance_km",
    "Shipment_Weight_kg",
    "Shipment_Volume",
    "Delivery_Time_hr",
    "Transportation_Cost"
]

for column in numerical_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        df[column] = df[column].fillna(
            df[column].median()
        )

# ---------------------------------------------------------
# 7. Handle missing categorical values
# ---------------------------------------------------------

for column in categorical_columns:
    if column in df.columns:
        df[column] = df[column].fillna("Unknown")

# ---------------------------------------------------------
# 8. Detect numerical outliers using IQR
# ---------------------------------------------------------

print("\nOUTLIER ANALYSIS")
print("=" * 50)

outlier_summary = {}

for column in numerical_columns:

    if column in df.columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        ]

        outlier_summary[column] = len(outliers)

        print(
            f"{column}: {len(outliers)} potential outliers"
        )

# ---------------------------------------------------------
# 9. Check missing values after cleaning
# ---------------------------------------------------------

print("\nMISSING VALUES AFTER CLEANING")
print("=" * 50)
print(df.isnull().sum())

# ---------------------------------------------------------
# 10. Display cleaned dataset information
# ---------------------------------------------------------

print("\nCLEANED DATASET")
print("=" * 50)

print(df.head())

print("\nCleaned Dataset Shape:")
print(df.shape)

# ---------------------------------------------------------
# 11. Save cleaned dataset
# ---------------------------------------------------------

df.to_csv(
    "logistics_cleaned_data.csv",
    index=False
)

print("\nCleaned dataset saved as:")
print("logistics_cleaned_data.csv")

# ---------------------------------------------------------
# 12. Final summary
# ---------------------------------------------------------

print("\nPREPROCESSING SUMMARY")
print("=" * 50)

print("✓ Duplicate records removed")
print("✓ Date values converted")
print("✓ Categorical values standardized")
print("✓ Missing numerical values handled")
print("✓ Missing categorical values handled")
print("✓ Potential outliers identified using IQR")
print("✓ Cleaned dataset exported successfully")
