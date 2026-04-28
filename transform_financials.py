import pandas as pd
import json

file_path = "bronze_layer/raw_financial_data.json"

with open(file_path, "r") as file:
    raw_financials = json.load(file)

# Reshape the nested dictionary into a list of rows
rows = []
for asset, prices in raw_financials.items():
    row = {
        "asset_name": asset.capitalize(),
        "price_usd": prices.get("usd"),
        "price_cad": prices.get("cad")
    }
    rows.append(row)

# Convert the list of rows into a DataFrame
df_financials = pd.DataFrame(rows)

silver_path = "silver_layer/financials_cleaned.csv"
df_financials.to_csv(silver_path, index=False)

print(f"Transformation complete! Clean financial data saved to {silver_path}")