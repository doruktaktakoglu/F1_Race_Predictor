import fastf1
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import os

# Enable FastF1 caching
os.makedirs("f1_cache", exist_ok=True)
fastf1.Cache.enable_cache("f1_cache")

# Load 2024 Miami Race Session
session_2024 = fastf1.get_session(2024, 'Miami', 'R')
session_2024.load()

# Extract and process race lap times
laps_2024 = session_2024.laps[["Driver", "LapTime"]].dropna().copy()
laps_2024["LapTime (s)"] = laps_2024["LapTime"].dt.total_seconds()

# Load 2025 Miami Qualifying Session
session_2025 = fastf1.get_session(2025, 'Miami', 'Q')
session_2025.load()

# Get all laps, calculate time in seconds
quali_laps = session_2025.laps.dropna(subset=["LapTime"]).copy()
quali_laps["QualifyingTime (s)"] = quali_laps["LapTime"].dt.total_seconds()

# Keep the fastest lap for each driver
fastest_quali = (
    quali_laps.sort_values(by=["Driver", "QualifyingTime (s)"])
    .drop_duplicates(subset="Driver")
    .reset_index(drop=True)
)

# Create 2025 qualifying DataFrame
qualifying_2025 = fastest_quali[["Driver", "QualifyingTime (s)"]].copy()
qualifying_2025["DriverCode"] = qualifying_2025["Driver"]  # 3-letter codes

# Merge 2025 quali with 2024 race lap data
merged_data = qualifying_2025.merge(laps_2024, left_on="DriverCode", right_on="Driver")

# Features and targets
X = merged_data[["QualifyingTime (s)"]]
y = merged_data["LapTime (s)"]

if X.empty:
    raise ValueError("No matching drivers found between 2025 quali and 2024 race.")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=39)

# Train model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=39)
model.fit(X_train, y_train)

# Predict race time using 2025 qualifying times
qualifying_2025["PredictedRaceTime (s)"] = model.predict(qualifying_2025[["QualifyingTime (s)"]])

# Sort by predicted race time
qualifying_2025 = qualifying_2025.sort_values(by="PredictedRaceTime (s)")

# Output predictions
print("\n🏁 Predicted 2025 Miami GP Ranking 🏁\n")
print(qualifying_2025[["Driver", "PredictedRaceTime (s)"]])

# Evaluation
y_pred = model.predict(X_test)
print(f"\n🔍 Model Error (MAE): {mean_absolute_error(y_test, y_pred):.2f} seconds")
