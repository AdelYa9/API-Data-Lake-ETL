import pandas as pd
import json

file_path = "bronze_layer/raw_weather_data.json"

with open(file_path, "r") as file:
    raw_weather = json.load(file)

current_weather = raw_weather["current_weather"]
df_weather = pd.json_normalize(current_weather)

df_weather["latitude"] = raw_weather["latitude"]
df_weather["longitude"] = raw_weather["longitude"]

silver_path = "silver_layer/weather_cleaned.csv"
df_weather.to_csv(silver_path, index=False)

print(f"Transformation complete! Clean weather data saved to {silver_path}")