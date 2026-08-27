# Week 4 – Predictive Modeling and Optimization in Logistics

## 1. Project Overview

This week focuses on applying predictive modeling and optimization techniques to a logistics dataset. The objective is to develop a predictive model capable of forecasting delivery time and use the model insights to propose strategies for improving logistics operations.

The project builds upon the data preparation and exploratory analysis performed during the previous weeks.

## 2. Problem Definition

The main problem addressed in this project is the prediction of shipment delivery time based on important logistics characteristics.

The target variable is:

- Delivery_Time_hr

The predictor variables include:

- Distance_km
- Shipment_Weight_kg
- Shipment_Volume
- Vehicle_Type
- Transportation_Cost
- Delivery_Status

Predicting delivery time can help logistics organizations improve planning, resource allocation, and delivery performance.

## 3. Methodology

The analysis follows these major steps:

1. Load the logistics dataset.
2. Prepare and preprocess the data.
3. Select relevant features.
4. Split the dataset into training and testing sets.
5. Train predictive regression models.
6. Evaluate model performance.
7. Compare prediction results.
8. Develop logistics optimization recommendations.

## 4. Predictive Modeling

Regression-based machine learning techniques are used to predict delivery time.

The models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

These metrics provide an understanding of prediction accuracy and model performance.

## 5. Optimization Strategy

The model results are used to identify opportunities for logistics optimization, including:

- Improving route planning.
- Reducing unnecessary transportation distance.
- Improving vehicle utilization.
- Optimizing shipment allocation.
- Reducing transportation costs.
- Improving delivery-time reliability.

## 6. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## 7. Expected Outcome

The project aims to develop a reliable predictive model for delivery time and translate the model findings into practical recommendations for improving logistics efficiency and operational performance.

## 8. Conclusion

Week 4 combines predictive analytics with logistics optimization to demonstrate how machine learning can support data-driven operational decision-making.



## 9. Results

### Predictive Modeling

Two regression models were trained to predict shipment delivery time:

- Linear Regression
- Random Forest Regressor

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was:

- **Best Model: Linear Regression**

Prediction results were saved in `week4_predictions.csv`, while model evaluation results were saved in `week4_model_results.csv`.

### Optimization Results

The optimization analysis identified:

- **Number of slow shipments: 75**
- **Best cost vehicle: Container**
- **Fastest vehicle: Container**

Optimization outputs were saved in:

- `week4_vehicle_optimization.csv`
- `week4_optimization_recommendations.csv`
- `week4_route_analysis.csv`

### Key Recommendations

1. Use vehicle types with lower average transportation cost for suitable shipment categories.
2. Prioritize shorter and more efficient routes.
3. Review high-cost shipments for better vehicle allocation and route planning.
4. Monitor slow deliveries and investigate operational causes.
5. Use predictive model outputs to anticipate delivery delays and improve resource allocation.