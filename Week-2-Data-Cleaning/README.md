
# Week 2 – Data Collection, Cleaning and Preprocessing

## 1. Project Overview

This week focuses on preparing logistics data for analysis and predictive modeling. The objective is to simulate a realistic logistics data collection process and develop a systematic data cleaning and preprocessing pipeline.

The dataset contains information about shipments, distances, shipment weights, vehicle types, shipment volumes, delivery times, transportation costs, and delivery status.

## 2. Data Collection

A hypothetical logistics dataset is used for this project. The dataset represents shipment-level operational information that could be collected from a logistics management system.

The main variables include:

- Shipment_ID
- Shipment_Date
- Origin
- Destination
- Distance_km
- Shipment_Weight_kg
- Vehicle_Type
- Shipment_Volume
- Delivery_Time_hr
- Transportation_Cost
- Delivery_Status

## 3. Data Quality Issues

The following potential data-quality problems were considered:

- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent categorical values
- Extreme numerical observations
- Invalid or inconsistent records

## 4. Data Cleaning Strategy

The preprocessing workflow includes:

1. Loading the dataset using pandas.
2. Inspecting the dataset structure.
3. Checking for missing values.
4. Identifying duplicate records.
5. Converting date columns into datetime format.
6. Standardizing categorical values.
7. Detecting potential outliers using the IQR method.
8. Handling missing numerical values using median imputation where appropriate.
9. Preparing numerical features for scaling when required.

## 5. Missing Value Treatment

Numerical missing values can be replaced using the median because the median is less sensitive to extreme observations than the mean.

Categorical missing values can be assigned an appropriate category such as "Unknown" when the original value cannot be determined.

## 6. Outlier Detection

The Interquartile Range (IQR) method is used to identify potential outliers.

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Outliers will not automatically be deleted because an extreme logistics observation may represent a genuine long-distance shipment, unusually large shipment, or high-cost delivery.

## 7. Data Preprocessing

After cleaning, the dataset will be transformed into an analysis-ready format.

Important preprocessing activities include:

- Removing duplicates
- Handling missing values
- Correcting data types
- Standardizing categorical variables
- Detecting extreme observations
- Scaling numerical variables when required

## 8. Python Libraries

The following Python libraries are used:

- pandas
- NumPy
- scikit-learn

## 9. Expected Outcome

The final output of this stage is a clean and structured logistics dataset suitable for exploratory data analysis and visualization in Week 3.

## 10. Week 2 Conclusion

Data quality is an important foundation for reliable logistics analytics. The cleaning and preprocessing workflow developed in this task reduces inconsistencies and prepares the dataset for further analysis. The processed data will be used in Week 3 to identify trends, relationships, and operational insights through exploratory data analysis and visualization.
