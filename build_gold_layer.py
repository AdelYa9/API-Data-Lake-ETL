import pandas as pd
import os
from datetime import datetime

df_drivers = pd.read_csv("silver_layer/drivers_cleaned.csv")
df_weather = pd.read_csv("silver_layer/weather_cleaned.csv")
df_financials = pd.read_csv("silver_layer/financials_cleaned.csv")

current_temp = df_weather["temperature"].iloc[0]
current_wind = df_weather["windspeed"].iloc[0]

btc_cad = df_financials.loc[df_financials['asset_name'] == 'Bitcoin', 'price_cad'].iloc[0]
eth_cad = df_financials.loc[df_financials['asset_name'] == 'Ethereum', 'price_cad'].iloc[0]

df_master = df_drivers.copy()

df_master["snapshot_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

df_master["hub_temp_c"] = current_temp
df_master["hub_windspeed"] = current_wind

df_master["macro_btc_cad"] = btc_cad
df_master["macro_eth_cad"] = eth_cad

os.makedirs("gold_layer", exist_ok=True)
gold_path = "gold_layer/master_logistics_snapshot.csv"
df_master.to_csv(gold_path, index=False)

print(f"Gold Layer complete! Master reporting table saved to {gold_path}")