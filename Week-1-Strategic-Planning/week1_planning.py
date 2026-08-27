
# Week 1 - Strategic Planning and Data Exploration in Logistics
# Yuva Intern - Logistics Data Analytics

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. Create a small simulated logistics dataset
# ---------------------------------------------------------

data = {
    "Shipment_ID": ["S001", "S002", "S003", "S004", "S005",
                    "S006", "S007", "S008", "S009", "S010"],

    "Distance_km": [120, 250, 85, 430, 175,
                    310, 95, 520, 210, 150],

    "Shipment_Weight_kg": [450, 800, 300, 1200, 650,
                           900, 250, 1500, 700, 500],

    "Vehicle_Type": ["Truck", "Truck", "Van", "Truck", "Van",
                     "Truck", "Van", "Truck", "Truck", "Van"],

    "Shipment_Volume": [12, 20, 8, 30, 15,
                        24, 7, 35, 18, 11],

    "Delivery_Time_hr": [4.5, 8.2, 3.1, 14.5, 6.4,
                         10.8, 3.5, 17.2, 7.6, 5.2],

    "Transportation_Cost": [3200, 6100, 2200, 10500, 4300,
                            7800, 2400, 12500, 5900, 3500],

    "Delivery_Status": ["On Time", "Delayed", "On Time", "Delayed",
                        "On Time", "Delayed", "On Time", "Delayed",
                        "On Time", "On Time"]
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# 2. Display basic dataset information
# ---------------------------------------------------------

print("LOGISTICS DATASET")
print("=" * 50)

print("\nFirst five records:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

# ---------------------------------------------------------
# 3. Calculate important logistics KPIs
# ---------------------------------------------------------

average_delivery_time = df["Delivery_Time_hr"].mean()

on_time_rate = (
    (df["Delivery_Status"] == "On Time").mean() * 100
)

total_transportation_cost = df["Transportation_Cost"].sum()

average_cost_per_shipment = df["Transportation_Cost"].mean()

shipment_volume = df["Shipment_Volume"].sum()

delay_rate = (
    (df["Delivery_Status"] == "Delayed").mean() * 100
)

print("\nKEY PERFORMANCE INDICATORS")
print("=" * 50)

print(f"Average Delivery Time: {average_delivery_time:.2f} hours")
print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")
print(f"Total Transportation Cost: ₹{total_transportation_cost:,.2f}")
print(f"Average Cost per Shipment: ₹{average_cost_per_shipment:,.2f}")
print(f"Total Shipment Volume: {shipment_volume}")
print(f"Delay Rate: {delay_rate:.2f}%")

# ---------------------------------------------------------
# 4. Compare delivery performance by vehicle type
# ---------------------------------------------------------

vehicle_performance = (
    df.groupby("Vehicle_Type")["Delivery_Time_hr"]
    .mean()
    .sort_values()
)

print("\nAVERAGE DELIVERY TIME BY VEHICLE")
print("=" * 50)
print(vehicle_performance)

# ---------------------------------------------------------
# 5. Identify delayed shipments
# ---------------------------------------------------------

delayed_shipments = df[
    df["Delivery_Status"] == "Delayed"
]

print("\nDELAYED SHIPMENTS")
print("=" * 50)
print(delayed_shipments[
    ["Shipment_ID", "Distance_km",
     "Vehicle_Type", "Delivery_Time_hr"]
])

# ---------------------------------------------------------
# 6. Initial strategic observations
# ---------------------------------------------------------

print("\nINITIAL STRATEGIC OBSERVATIONS")
print("=" * 50)

print("1. Longer routes generally require more delivery time.")
print("2. Longer routes also tend to have higher transportation costs.")
print("3. Delayed shipments should be investigated for route and")
print("   resource optimization opportunities.")
print("4. Vehicle-level performance can support better vehicle allocation.")
print("5. Delivery-time prediction can help improve logistics planning.")

# ---------------------------------------------------------
# 7. Planned analytical roadmap
# ---------------------------------------------------------

roadmap = [
    "Data Collection",
    "Data Cleaning and Preprocessing",
    "Exploratory Data Analysis",
    "Data Visualization",
    "Predictive Modeling",
    "Model Evaluation",
    "Logistics Optimization",
    "Business Recommendations"
]

print("\nPROJECT ROADMAP")
print("=" * 50)

for step, activity in enumerate(roadmap, start=1):
    print(f"{step}. {activity}")
