# IoT Sensor Data ETL Pipeline

A Python and MySQL-based ETL pipeline that extracts IoT sensor readings from CSV files, cleans and transforms the data, and loads it into a MySQL database for analysis.

## Project Overview

This project demonstrates a basic ETL (Extract, Transform, Load) workflow using IoT sensor data. It processes temperature and humidity readings collected from different locations and stores the cleaned records in a MySQL database.

## Technologies Used

- **Programming Language:** Python
- **Database:** MySQL
- **Database Connectivity:** MySQL Connector/Python
- **Data Processing:** Python CSV module
- **Tools:** VS Code, MySQL

## Project Structure

```text
IoT_ETL_Project/
│
├── data/
│   └── sensor_data.csv
│
├── main.py
├── database.py
├── iot_etl_database.sql
├── requirements.txt
└── README.md
```

## ETL Workflow

### 1. Extract
- Read IoT sensor records from a CSV file.
- Extract sensor ID, temperature, humidity and location.

### 2. Transform
- Identify and remove duplicate records.
- Handle missing temperature and humidity values.
- Convert sensor readings into appropriate numeric data types.

### 3. Load
- Connect Python to MySQL using MySQL Connector.
- Insert cleaned records into the `sensor_readings` table.
- Prevent duplicate sensor records using a UNIQUE constraint and `INSERT IGNORE`.

## Database Structure

**Database:** `iot_etl_db`

**Table:** `sensor_readings`

| Column | Data Type | Description |
|---|---|---|
| id | INT | Primary key |
| sensor_id | VARCHAR(20) | Sensor identifier |
| temperature | FLOAT | Temperature reading |
| humidity | FLOAT | Humidity reading |
| location | VARCHAR(50) | Sensor location |

## Data Analysis

SQL queries were used to perform the following analysis:

- Calculate average temperature.
- Identify the maximum temperature.
- Calculate average humidity.
- Count sensor readings by location.
- Retrieve readings where temperature exceeds 30°C.

## Sample Results

| Metric | Result |
|---|---:|
| Total cleaned records | 7 |
| Average temperature | 29.49°C |
| Average humidity | 67.57% |
| Maximum temperature | 32.10°C |

## Installation and Execution

### Prerequisites
- Python 3.10 or later
- MySQL Server
- MySQL Connector/Python

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/IoT-Sensor-Data-ETL-Pipeline.git
```

### Step 2: Navigate to the project directory

```bash
cd IoT-Sensor-Data-ETL-Pipeline
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create the database

Run the SQL script:

```text
iot_etl_database.sql
```

### Step 5: Configure database credentials

Update the MySQL connection settings in `database.py` with your local MySQL credentials. Do not commit passwords or other secrets to GitHub.

### Step 6: Run the ETL pipeline

```bash
python main.py
```

## Key Features

- CSV-based data extraction.
- Data cleaning and transformation.
- MySQL database integration.
- Duplicate record prevention.
- SQL-based data analysis.

## Future Improvements

- Integrate real-time IoT sensor data.
- Add data visualisation.
- Support multiple sensor data sources.
- Automate ETL execution.

## Author

**Rittika Kundu**



