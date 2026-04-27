# Project Nexus: API Data Lake Extraction Pipeline

## The Business Scenario
A mid-sized North American logistics and delivery startup is experiencing unexplained spikes in delivery delays and operational costs. Executive leadership suspects that regional weather events and macro-economic shifts are impacting driver efficiency, but their internal data is currently siloed across different systems. 

## The Objective
Architect an automated Data Lake using the Medallion Architecture to break down these data silos. This project programmatically extracts live data from multiple external APIs, centralizes the raw JSON payloads into a Bronze storage layer, and prepares the data for downstream BI reporting and predictive modeling.

## Data Sources
* **Operations Data (RandomUser API):** Simulates internal CRM data, extracting driver profiles, geographical coordinates, and status.
* **Environmental Data (Open-Meteo API):** Captures live, localized weather conditions for key logistics hubs to correlate with transit delays.
* **Macro-Economic Data (CoinGecko API):** Tracks real-time financial market fluctuations as a proxy for shifting operational overhead.

## Technical Stack
* **Language:** Python
* **Data Architecture:** REST API Integration, JSON Data Parsing, Data Lake Design
* **Libraries:** `requests`, `json`