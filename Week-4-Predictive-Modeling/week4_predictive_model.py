# ============================================================
# Week 4 - Predictive Modeling in Logistics
# YUVA Internship - Logistics Data Analytics
# ============================================================

import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


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
df = df.dropna()

print("=" * 60)
print("WEEK 4 - PREDICTIVE MODELING")
print("=" * 60)

print("\nDataset loaded successfully.")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 2. DATA PREPARATION
# ============================================================

df = df.drop_duplicates()

# Remove rows where target variable is missing
df = df.dropna(subset=["Delivery_Time_hr"])

print("\nDataset after cleaning:")
print(df.shape)


# ============================================================
# 3. DEFINE FEATURES AND TARGET
# ============================================================

target = "Delivery_Time_hr"

features = [
    "Distance_km",
    "Shipment_Weight_kg",
    "Shipment_Volume",
    "Vehicle_Type",
    "Transportation_Cost"
]

X = df[features]
y = df[target]

print("\nTarget variable:")
print(target)

print("\nPredictor variables:")
for feature in features:
    print("-", feature)


# ============================================================
# 4. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ============================================================
# 5. PREPROCESSING
# ============================================================

categorical_features = ["Vehicle_Type"]

numeric_features = [
    "Distance_km",
    "Shipment_Weight_kg",
    "Shipment_Volume",
    "Transportation_Cost"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)


# ============================================================
# 6. LINEAR REGRESSION MODEL
# ============================================================

linear_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ]
)

linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)


# ============================================================
# 7. RANDOM FOREST MODEL
# ============================================================

random_forest_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)

random_forest_model.fit(X_train, y_train)

rf_predictions = random_forest_model.predict(X_test)


# ============================================================
# 8. MODEL EVALUATION FUNCTION
# ============================================================

def evaluate_model(model_name, actual, predicted):

    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual, predicted)

    print("\n" + "-" * 50)
    print(model_name)
    print("-" * 50)

    print("MAE  :", round(mae, 2))
    print("MSE  :", round(mse, 2))
    print("RMSE :", round(rmse, 2))
    print("R²   :", round(r2, 2))

    return {
        "Model": model_name,
        "MAE": round(mae, 2),
        "MSE": round(mse, 2),
        "RMSE": round(rmse, 2),
        "R2": round(r2, 2)
    }


# ============================================================
# 9. EVALUATE MODELS
# ============================================================

linear_results = evaluate_model(
    "Linear Regression",
    y_test,
    linear_predictions
)

rf_results = evaluate_model(
    "Random Forest",
    y_test,
    rf_predictions
)


# ============================================================
# 10. COMPARE MODELS
# ============================================================

results = pd.DataFrame(
    [linear_results, rf_results]
)

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(results)


# ============================================================
# 11. SELECT BEST MODEL
# ============================================================

best_model_row = results.loc[
    results["RMSE"].idxmin()
]

best_model_name = best_model_row["Model"]

print("\nBest Model:", best_model_name)


# ============================================================
# 12. SAVE MODEL RESULTS
# ============================================================

results.to_csv(
    "week4_model_results.csv",
    index=False
)

print("\nModel results saved as:")
print("week4_model_results.csv")


# ============================================================
# 13. CREATE PREDICTION OUTPUT
# ============================================================

prediction_output = X_test.copy()

prediction_output["Actual_Delivery_Time_hr"] = y_test.values

prediction_output["Linear_Regression_Prediction"] = (
    linear_predictions
)

prediction_output["Random_Forest_Prediction"] = (
    rf_predictions
)

prediction_output.to_csv(
    "week4_predictions.csv",
    index=False
)

print("\nPredictions saved as:")
print("week4_predictions.csv")


# ============================================================
# 14. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("WEEK 4 PREDICTIVE MODELING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nModels trained:")
print("- Linear Regression")
print("- Random Forest Regressor")

print("\nEvaluation metrics:")
print("- MAE")
print("- MSE")
print("- RMSE")
print("- R²")

print("\nGenerated files:")
print("- week4_model_results.csv")
print("- week4_predictions.csv")

print("\nBest model:", best_model_name)

print("=" * 60)
