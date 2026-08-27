# ============================================================
# Week 4 - Logistics Optimization
# YUVA Internship - Logistics Data Analytics
# ============================================================

import os
import pandas as pd
import numpy as np


# ============================================================
# 1. LOAD DATASET
# ============================================================

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
        "logistics_raw_data.csv was not found."
    )

df = pd.read_csv(file_path)

print("=" * 60)
print("WEEK 4 - LOGISTICS OPTIMIZATION")
print("=" * 60)

print("\nDataset loaded successfully.")
print("Records:", len(df))


# ============================================================
# 2. BASIC DATA PREPARATION
# ============================================================

df = df.drop_duplicates()

df = df.dropna(
    subset=[
        "Distance_km",
        "Shipment_Weight_kg",
        "Shipment_Volume",
        "Transportation_Cost",
        "Delivery_Time_hr"
    ]
)

print("Records after cleaning:", len(df))


# ============================================================
# 3. LOGISTICS PERFORMANCE ANALYSIS
# ============================================================

df["Cost_per_km"] = (
    df["Transportation_Cost"] /
    df["Distance_km"]
)

df["Cost_per_kg"] = (
    df["Transportation_Cost"] /
    df["Shipment_Weight_kg"]
)

df["Delivery_Efficiency"] = (
    df["Distance_km"] /
    df["Delivery_Time_hr"]
)


# ============================================================
# 4. VEHICLE TYPE ANALYSIS
# ============================================================

vehicle_summary = (
    df.groupby("Vehicle_Type")
    .agg(
        Average_Delivery_Time_hr=(
            "Delivery_Time_hr",
            "mean"
        ),
        Average_Transportation_Cost=(
            "Transportation_Cost",
            "mean"
        ),
        Average_Distance_km=(
            "Distance_km",
            "mean"
        ),
        Average_Shipment_Weight_kg=(
            "Shipment_Weight_kg",
            "mean"
        ),
        Number_of_Shipments=(
            "Shipment_ID",
            "count"
        )
    )
    .round(2)
)

print("\n" + "=" * 60)
print("VEHICLE PERFORMANCE")
print("=" * 60)

print(vehicle_summary)


# ============================================================
# 5. IDENTIFY MOST COST-EFFICIENT VEHICLE
# ============================================================

best_cost_vehicle = (
    vehicle_summary[
        "Average_Transportation_Cost"
    ].idxmin()
)

best_time_vehicle = (
    vehicle_summary[
        "Average_Delivery_Time_hr"
    ].idxmin()
)

print("\nMost cost-efficient vehicle type:")
print(best_cost_vehicle)

print("\nFastest vehicle type:")
print(best_time_vehicle)


# ============================================================
# 6. ROUTE / SHIPMENT ANALYSIS
# ============================================================

route_columns = []

if "Origin" in df.columns:
    route_columns.append("Origin")

if "Destination" in df.columns:
    route_columns.append("Destination")

if route_columns:
    route_summary = (
        df.groupby(route_columns)
        .agg(
            Average_Cost=(
                "Transportation_Cost",
                "mean"
            ),
            Average_Delivery_Time=(
                "Delivery_Time_hr",
                "mean"
            ),
            Shipment_Count=(
                "Shipment_ID",
                "count"
            )
        )
        .reset_index()
        .round(2)
    )

    print("\n" + "=" * 60)
    print("ROUTE ANALYSIS")
    print("=" * 60)

    print(route_summary)

    route_summary.to_csv(
        "week4_route_analysis.csv",
        index=False
    )


# ============================================================
# 7. IDENTIFY HIGH-COST SHIPMENTS
# ============================================================

cost_threshold = df["Transportation_Cost"].quantile(0.75)

high_cost_shipments = df[
    df["Transportation_Cost"] >= cost_threshold
].copy()

print("\n" + "=" * 60)
print("HIGH-COST SHIPMENTS")
print("=" * 60)

print(
    "High-cost threshold:",
    round(cost_threshold, 2)
)

print(
    "Number of high-cost shipments:",
    len(high_cost_shipments)
)


# ============================================================
# 8. IDENTIFY SLOW DELIVERIES
# ============================================================

delivery_threshold = (
    df["Delivery_Time_hr"].quantile(0.75)
)

slow_shipments = df[
    df["Delivery_Time_hr"] >= delivery_threshold
].copy()

print("\nSlow delivery threshold:")
print(round(delivery_threshold, 2), "hours")

print(
    "Number of slow shipments:",
    len(slow_shipments)
)


# ============================================================
# 9. OPTIMIZATION RECOMMENDATIONS
# ============================================================

recommendations = []

recommendations.append(
    "Use vehicle types with lower average transportation cost "
    "for suitable shipment categories."
)

recommendations.append(
    "Prioritize shorter and more efficient routes where possible "
    "to reduce delivery time."
)

recommendations.append(
    "Review high-cost shipments to identify opportunities for "
    "better vehicle allocation and route planning."
)

recommendations.append(
    "Monitor slow deliveries and investigate operational causes "
    "such as long distances, high shipment volume, or vehicle constraints."
)

recommendations.append(
    "Use predictive model outputs to anticipate delivery delays "
    "and improve resource allocation."
)


# ============================================================
# 10. SAVE OPTIMIZATION RECOMMENDATIONS
# ============================================================

recommendation_df = pd.DataFrame({
    "Recommendation": recommendations
})

recommendation_df.to_csv(
    "week4_optimization_recommendations.csv",
    index=False
)


# ============================================================
# 11. SAVE VEHICLE SUMMARY
# ============================================================

vehicle_summary.reset_index().to_csv(
    "week4_vehicle_optimization.csv",
    index=False
)


# ============================================================
# 12. FINAL OUTPUT
# ============================================================

print("\n" + "=" * 60)
print("OPTIMIZATION RECOMMENDATIONS")
print("=" * 60)

for i, recommendation in enumerate(
    recommendations,
    start=1
):
    print(f"{i}. {recommendation}")


print("\n" + "=" * 60)
print("WEEK 4 OPTIMIZATION COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated files:")
print("- week4_vehicle_optimization.csv")
print("- week4_optimization_recommendations.csv")

if route_columns:
    print("- week4_route_analysis.csv")

print("\nBest cost vehicle:", best_cost_vehicle)
print("Fastest vehicle:", best_time_vehicle)

print("=" * 60)
