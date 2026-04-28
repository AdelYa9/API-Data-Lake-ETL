import pandas as pd
import json
import os

# 1. Load the raw JSON from the Bronze Layer
file_path = "bronze_layer/raw_drivers_data.json"
with open(file_path, "r") as file:
    raw_data = json.load(file)

# 2. Flatten the nested JSON into a tabular DataFrame
# The randomuser API stores the actual driver list inside a "results" key
df = pd.json_normalize(raw_data["results"])

# 3. Select only the columns we care about for the logistics scenario
columns_to_keep = [
    "login.uuid", 
    "name.first", 
    "name.last", 
    "email", 
    "location.coordinates.latitude", 
    "location.coordinates.longitude"
]
df_clean = df[columns_to_keep]

# 4. Rename the columns to standard SQL-friendly naming conventions
df_clean.columns = [
    "driver_id", 
    "first_name", 
    "last_name", 
    "email", 
    "latitude", 
    "longitude"
]

# 5. Save the clean tabular data to the Silver Layer
os.makedirs("silver_layer", exist_ok=True)
silver_path = "silver_layer/drivers_cleaned.csv"
df_clean.to_csv(silver_path, index=False)

print(f"Transformation complete! Clean data saved to {silver_path}")