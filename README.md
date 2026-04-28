# Project Nexus: API Data Lake Extraction Pipeline

## The Business Scenario
A mid-sized North American logistics and delivery startup is experiencing unexplained spikes in delivery delays and operational costs. Executive leadership suspects that regional weather events and macro-economic shifts are impacting driver efficiency, but their internal data is currently siloed across different systems. 

## The Objective
Design an automated DataOps pipeline to break down these data silos. This project programmatically extracts live external data, centralizes it into a local storage environment, and structures it for immediate downstream Business Intelligence reporting and predictive modeling.

## Data Sources
* **Operations Data (RandomUser API):** Simulates internal CRM data, extracting driver profiles, geographical coordinates, and deployment status.
* **Environmental Data (Open-Meteo API):** Captures live, localized weather conditions for key logistics hubs (e.g., Calgary, AB) to correlate with transit delays.
* **Macro-Economic Data (CoinGecko API):** Tracks real-time financial market fluctuations (BTC and ETH in CAD) as a proxy for shifting operational overhead.

## Technical Stack
* **Language:** Python
* **Data Architecture:** Medallion Data Lake (Bronze, Silver, Gold), REST API Integration, JSON Parsing
* **Libraries:** `requests`, `pandas`, `json`, `os`, `datetime`

## Pipeline Architecture
* **Bronze (Raw Ingestion):** Automated HTTP GET requests extract live, heavily nested JSON payloads, landing them securely in local storage without mutation to preserve data lineage.
* **Silver (Transformation & Cleansing):** `pandas` is utilized to flatten hierarchical dictionaries into 2D tables. During this phase, schemas are standardized (snake_case), parent-level metadata is mapped to individual rows, and API noise is filtered to retain only business-critical fields.
* **Gold (Business Aggregation):** Independent data streams are joined into a single "Point-in-Time" snapshot. Disparate data grains (individual drivers vs. regional weather vs. global crypto prices) are unified into a denormalized master table.

## Business Value & Final Deliverable
The resulting `master_logistics_snapshot.csv` is a completely BI-ready artifact. By shifting the transformation workload upstream into Python, this architecture eliminates the need for complex, computationally expensive DAX modeling in the BI layer. Analytics teams can immediately connect Power BI to this flat file to visualize correlations between fleet deployment, weather systems, and macro-economic overhead.

## Cloud Automation & CI/CD
To transition this project from a local script to an enterprise-grade DataOps pipeline, the entire ETL process is fully automated using **GitHub Actions**.

* **Serverless Execution:** A YAML-based CI/CD workflow automatically provisions an Ubuntu cloud environment, installs required dependencies, and executes the Medallion pipeline sequentially.
* **Scheduled Ingestion:** The workflow is triggered by a daily CRON schedule (8:00 AM UTC), ensuring the Gold layer reporting table is consistently refreshed with the latest point-in-time snapshot.
* **Automated Commits:** Upon successful data aggregation, a configured Actions bot automatically commits the fresh Bronze, Silver, and Gold datasets and pushes them directly to the main branch, maintaining a fully autonomous data lifecycle with zero manual intervention.