import requests
import json
import os

# CoinGecko API requesting BTC and ETH prices in USD and CAD
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,cad"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    os.makedirs("bronze_layer", exist_ok=True)
    
    file_path = "bronze_layer/raw_financial_data.json"
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        
    print(f"Success! Raw financial data saved to {file_path}")
else:
    print(f"API Connection Failed. Status Code: {response.status_code}")