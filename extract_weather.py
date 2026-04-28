import requests
import json
import os

url = "https://api.open-meteo.com/v1/forecast?latitude=51.0447&longitude=-114.0719&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    os.makedirs("bronze_layer", exist_ok=True)
    
    file_path = "bronze_layer/raw_weather_data.json"
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        
    print(f"Success! Raw weather data saved to {file_path}")
else:
    print(f"API Connection Failed. Status Code: {response.status_code}")