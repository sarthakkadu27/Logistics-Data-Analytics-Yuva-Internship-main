
# Week 3 – Advanced Data Analysis and Visualization in Logistics

## 1. Project Overview

This week focuses on performing exploratory data analysis (EDA) and visualization on a logistics dataset. The objective is to understand shipment patterns, delivery performance, transportation costs, and relationships between important operational variables.

The analysis uses Python and common data analysis libraries to explore the dataset and identify useful patterns that can support logistics decision-making.

---

## 2. Dataset Description

The logistics dataset contains shipment-level operational information.

The major variables include:

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

These variables provide information about shipment characteristics, transportation requirements, delivery performance, and operational costs.

---

## 3. Exploratory Data Analysis

The following EDA activities are performed:

- Inspection of dataset structure and data types
- Calculation of descriptive statistics
- Identification of missing values
- Analysis of numerical variables
- Analysis of categorical variables
- Examination of delivery-time patterns
- Analysis of transportation costs
- Comparison of different vehicle types
- Analysis of shipment volume and weight
- Correlation analysis between numerical variables

Python libraries such as Pandas and NumPy are used for data exploration and statistical analysis.

---

## 4. Data Visualizations

Multiple visualizations are created to understand the logistics data more effectively.

The planned visualizations include:

### 4.1 Shipment Volume Distribution

A histogram is used to understand the distribution of shipment volumes.

### 4.2 Delivery Time Distribution

A histogram is used to analyze the distribution of delivery times and identify possible variations in delivery performance.

### 4.3 Transportation Cost Analysis

A bar chart is used to compare transportation costs across shipment categories.

### 4.4 Vehicle Type Analysis

A count plot is used to compare the number of shipments handled by different vehicle types.

### 4.5 Distance vs Delivery Time

A scatter plot is used to examine whether longer transportation distances are associated with higher delivery times.

### 4.6 Distance vs Transportation Cost

A scatter plot is used to investigate the relationship between transportation distance and transportation cost.

### 4.7 Correlation Heatmap

A correlation heatmap is used to identify relationships between numerical variables such as distance, shipment weight, shipment volume, delivery time, and transportation cost.

---

## 5. Analytical Insights

The analysis is designed to identify important logistics patterns, including:

- Factors that influence delivery time
- Relationship between transportation distance and delivery time
- Relationship between distance and transportation cost
- Effect of shipment characteristics on logistics operations
- Differences in operational performance across vehicle types
- Potential cost and efficiency bottlenecks

These insights can help logistics managers make better decisions regarding transportation planning, resource allocation, and operational efficiency.

---

## 6. Business Recommendations

Based on the findings from the analysis, possible recommendations include:

- Optimizing vehicle allocation based on shipment requirements
- Monitoring routes with unusually high delivery times
- Identifying cost-intensive transportation activities
- Improving resource allocation for high-volume shipments
- Using historical logistics patterns to improve delivery planning
- Monitoring key operational performance indicators regularly

---

## 7. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 8. Conclusion

The exploratory analysis provides a better understanding of logistics operations by examining shipment characteristics, delivery performance, transportation costs, and relationships among important variables.

The visualizations make the analysis easier to interpret and help identify operational patterns and potential areas for improvement. The findings from this week will also provide a foundation for predictive modeling and optimization activities in Week 4.

---

## 9. Python Analysis

The complete Python implementation for data analysis and visualization is provided in:

`week3_analysis.py`
