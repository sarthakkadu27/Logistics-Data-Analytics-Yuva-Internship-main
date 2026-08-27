# ============================================================
# Week 3 - Advanced Data Analysis and Visualization
# YUVA Intern - Logistics Data Analytics
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. LOAD DATASET
# ============================================================

# Possible locations of the logistics dataset
possible_paths = [
    "../Week-2-Data-Cleaning/logistics_raw_data.csv",
    "../logistics_raw_data.csv",
    "logistics_raw_data.csv",
    "Week-2-Data-Cleaning/logistics_raw_data.csv"
]

file_path = None

for path in possible_paths:
    if os.path.exists(path):
        file_path = path
        break

if file_path is None:
    raise FileNotFoundError(
        "logistics_raw_data.csv was not found. "
        "Please check the dataset location."
    )

df = pd.read_csv(file_path)

print("=" * 60)
print("WEEK 3 - LOGISTICS EDA AND VISUALIZATION")
print("=" * 60)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)


# ============================================================
# 2. BASIC DATA EXPLORATION
# ============================================================

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Descriptive Statistics ---")
print(df.describe(include="all"))


# ============================================================
# 3. MISSING VALUE ANALYSIS
# ============================================================

print("\n--- Missing Values ---")
missing_values = df.isnull().sum()
print(missing_values)

print("\nTotal missing values:", df.isnull().sum().sum())


# ============================================================
# 4. DUPLICATE CHECK
# ============================================================

print("\n--- Duplicate Records ---")
duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)


# ============================================================
# 5. NUMERICAL SUMMARY
# ============================================================

numeric_columns = df.select_dtypes(include=np.number).columns

print("\n--- Numerical Columns ---")
print(numeric_columns.tolist())

print("\n--- Numerical Summary ---")
print(df[numeric_columns].describe())


# ============================================================
# 6. CATEGORICAL ANALYSIS
# ============================================================

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns

print("\n--- Categorical Columns ---")
print(categorical_columns.tolist())

for column in categorical_columns:
    print("\nValue counts for:", column)
    print(df[column].value_counts())


# ============================================================
# 7. VEHICLE TYPE ANALYSIS
# ============================================================

if "Vehicle_Type" in df.columns:

    print("\n--- Vehicle Type Analysis ---")
    vehicle_counts = df["Vehicle_Type"].value_counts()
    print(vehicle_counts)

    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="Vehicle_Type")
    plt.title("Shipment Count by Vehicle Type")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()

    plt.savefig("vehicle_type_distribution.png", dpi=300)
    plt.show()


# ============================================================
# 8. SHIPMENT VOLUME DISTRIBUTION
# ============================================================

if "Shipment_Volume" in df.columns:

    plt.figure(figsize=(8, 5))
    sns.histplot(
        df["Shipment_Volume"],
        bins=10,
        kde=True
    )

    plt.title("Shipment Volume Distribution")
    plt.xlabel("Shipment Volume")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig("shipment_volume_distribution.png", dpi=300)
    plt.show()


# ============================================================
# 9. DELIVERY TIME DISTRIBUTION
# ============================================================

if "Delivery_Time_hr" in df.columns:

    plt.figure(figsize=(8, 5))
    sns.histplot(
        df["Delivery_Time_hr"],
        bins=10,
        kde=True
    )

    plt.title("Delivery Time Distribution")
    plt.xlabel("Delivery Time (Hours)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig("delivery_time_distribution.png", dpi=300)
    plt.show()


# ============================================================
# 10. TRANSPORTATION COST ANALYSIS
# ============================================================

if "Transportation_Cost" in df.columns:

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="Shipment_ID",
        y="Transportation_Cost"
    )

    plt.title("Transportation Cost by Shipment")
    plt.xlabel("Shipment ID")
    plt.ylabel("Transportation Cost")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("transportation_cost_analysis.png", dpi=300)
    plt.show()


# ============================================================
# 11. DISTANCE VS DELIVERY TIME
# ============================================================

if "Distance_km" in df.columns and "Delivery_Time_hr" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Distance_km",
        y="Delivery_Time_hr",
        s=100
    )

    plt.title("Distance vs Delivery Time")
    plt.xlabel("Distance (km)")
    plt.ylabel("Delivery Time (Hours)")
    plt.tight_layout()

    plt.savefig("distance_vs_delivery_time.png", dpi=300)
    plt.show()


# ============================================================
# 12. DISTANCE VS TRANSPORTATION COST
# ============================================================

if "Distance_km" in df.columns and "Transportation_Cost" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Distance_km",
        y="Transportation_Cost",
        s=100
    )

    plt.title("Distance vs Transportation Cost")
    plt.xlabel("Distance (km)")
    plt.ylabel("Transportation Cost")
    plt.tight_layout()

    plt.savefig("distance_vs_transportation_cost.png", dpi=300)
    plt.show()


# ============================================================
# 13. SHIPMENT WEIGHT VS DELIVERY TIME
# ============================================================

if "Shipment_Weight_kg" in df.columns and "Delivery_Time_hr" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Shipment_Weight_kg",
        y="Delivery_Time_hr",
        s=100
    )

    plt.title("Shipment Weight vs Delivery Time")
    plt.xlabel("Shipment Weight (kg)")
    plt.ylabel("Delivery Time (Hours)")
    plt.tight_layout()

    plt.savefig("weight_vs_delivery_time.png", dpi=300)
    plt.show()


# ============================================================
# 14. CORRELATION ANALYSIS
# ============================================================

if len(numeric_columns) > 1:

    correlation_matrix = df[numeric_columns].corr()

    print("\n--- Correlation Matrix ---")
    print(correlation_matrix.round(2))

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap of Logistics Variables")
    plt.tight_layout()

    plt.savefig("correlation_heatmap.png", dpi=300)
    plt.show()


# ============================================================
# 15. KEY LOGISTICS METRICS
# ============================================================

print("\n" + "=" * 60)
print("KEY LOGISTICS METRICS")
print("=" * 60)

if "Distance_km" in df.columns:
    print(
        "Average Distance:",
        round(df["Distance_km"].mean(), 2),
        "km"
    )

if "Shipment_Weight_kg" in df.columns:
    print(
        "Average Shipment Weight:",
        round(df["Shipment_Weight_kg"].mean(), 2),
        "kg"
    )

if "Shipment_Volume" in df.columns:
    print(
        "Average Shipment Volume:",
        round(df["Shipment_Volume"].mean(), 2)
    )

if "Delivery_Time_hr" in df.columns:
    print(
        "Average Delivery Time:",
        round(df["Delivery_Time_hr"].mean(), 2),
        "hours"
    )

if "Transportation_Cost" in df.columns:
    print(
        "Average Transportation Cost:",
        round(df["Transportation_Cost"].mean(), 2)
    )


# ============================================================
# 16. ADDITIONAL INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("ANALYTICAL INSIGHTS")
print("=" * 60)

if "Delivery_Time_hr" in df.columns:

    fastest = df.loc[
        df["Delivery_Time_hr"].idxmin()
    ]

    slowest = df.loc[
        df["Delivery_Time_hr"].idxmax()
    ]

    print(
        "\nFastest Delivery:",
        fastest["Delivery_Time_hr"],
        "hours"
    )

    print(
        "Slowest Delivery:",
        slowest["Delivery_Time_hr"],
        "hours"
    )


if "Transportation_Cost" in df.columns:

    highest_cost = df.loc[
        df["Transportation_Cost"].idxmax()
    ]

    lowest_cost = df.loc[
        df["Transportation_Cost"].idxmin()
    ]

    print(
        "\nHighest Transportation Cost:",
        highest_cost["Transportation_Cost"]
    )

    print(
        "Lowest Transportation Cost:",
        lowest_cost["Transportation_Cost"]
    )


# ============================================================
# 17. SAVE SUMMARY STATISTICS
# ============================================================

summary = df[numeric_columns].describe().round(2)

summary.to_csv("week3_summary_statistics.csv")

print("\nSummary statistics saved as:")
print("week3_summary_statistics.csv")


# ============================================================
# 18. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("WEEK 3 ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated visualization files:")
print("- vehicle_type_distribution.png")
print("- shipment_volume_distribution.png")
print("- delivery_time_distribution.png")
print("- transportation_cost_analysis.png")
print("- distance_vs_delivery_time.png")
print("- distance_vs_transportation_cost.png")
print("- weight_vs_delivery_time.png")
print("- correlation_heatmap.png")

print("\nThe analysis provides insights into:")
print("- Shipment patterns")
print("- Delivery performance")
print("- Transportation costs")
print("- Vehicle utilization")
print("- Relationships between logistics variables")
print("- Potential operational bottlenecks")
