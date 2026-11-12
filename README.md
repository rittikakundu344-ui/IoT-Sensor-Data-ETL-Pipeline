IoT Sensor Data ETL Pipeline
Extract. Transform. Load. Analyse IoT sensor data with Python and MySQL.
A Python-based ETL project that processes IoT sensor readings from CSV
files, performs data cleaning and transformation, and loads structured
data into a MySQL database for analysis.




📌 About the Project
The IoT Sensor Data ETL Pipeline demonstrates a basic data
engineering workflow using Python and MySQL.

The project reads sensor data from a CSV file, cleans and transforms the
records, and stores the processed data in a MySQL database.

The dataset contains sensor IDs, temperature readings, humidity
readings, and location information.
✨ Features
- 📂 Extract sensor records from CSV files.
- 🧹 Handle missing temperature and humidity values.
- 🔄 Identify and remove duplicate records.
- 🔢 Convert sensor readings into numeric data types.
- 🗄️ Load cleaned data into a MySQL database.
- 🔐 Prevent duplicate database entries using a UNIQUE constraint and
  INSERT IGNORE.
- 📊 Analyse sensor readings using SQL queries.
- 📍 Summarise sensor data by location.
🔄 ETL Workflow
The pipeline follows three main stages:
1. Extract: Read sensor records from the CSV dataset using Python's
   CSV module.
2. Transform: Remove duplicates, handle missing values, and convert
   data types.
3. Load: Insert the cleaned records into the MySQL database.
ETL Process
       CSV Dataset
            |
            v
    Python Extraction
            |
            v
    Data Transformation
    - Remove duplicates
    - Handle missing values
    - Convert data types
            |
            v
      Cleaned Data
            |
            v
      MySQL Database
            |
            v
       SQL Analysis
🧱 Database Structure
Database Name: iot_etl_db

Table Name: sensor_readings

  Column          Data Type     Description
  id            INT           Auto-increment primary key
sensor_id     VARCHAR(20)   Unique sensor identifier
temperature   FLOAT         Temperature reading
humidity      FLOAT         Humidity reading
location      VARCHAR(50)   Sensor location
🔗 Database Constraints
- id is the primary key.
- sensor_id has a UNIQUE constraint to prevent duplicate sensor
  entries.
- INSERT IGNORE is used during data loading to skip duplicate
  entries.
🛠️ Technologies Used
- Python --- ETL processing and data transformation.
- MySQL --- relational database for storing cleaned sensor data.
- MySQL Connector/Python --- Python-to-MySQL connectivity.
- CSV Module --- reading and processing CSV records.
- VS Code --- development environment.
📂 Repository Contents
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
🚀 Getting Started
Prerequisites
- Python 3.10 or later
- MySQL Server
- MySQL Workbench (recommended)
Setup Instructions
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/IoT-Sensor-Data-ETL-Pipeline.git
2. Navigate to the project directory
cd IoT-Sensor-Data-ETL-Pipeline
3. Install dependencies
pip install -r requirements.txt
4. Create the database

Open MySQL Workbench and execute the iot_etl_database.sql script.

5. Configure database credentials

Update the MySQL connection settings in database.py with your local
database credentials. Do not upload passwords or other secrets to
GitHub.

6. Run the ETL pipeline
python main.py
🔍 Data Analysis
The project uses SQL queries to analyse the cleaned sensor records.

The following operations are performed:
- Calculate average temperature.
- Find the maximum temperature.
- Calculate average humidity.
- Count sensor readings by location.
- Retrieve sensor readings where temperature exceeds 30°C.
📊 Sample Results
The following results were obtained from the processed dataset:

  Metric                     Result
  Total cleaned records           7
Average temperature       29.49°C
Average humidity           67.57%
Maximum temperature       32.10°C
🎯 Project Objective
The objective of this project is to understand and implement the
fundamental concepts of data engineering, including data extraction,
data cleaning, transformation, database integration, and SQL-based
analysis.
🔮 Possible Future Improvements
- Integrate real-time IoT sensor data.
- Process data from multiple sensor sources.
- Automate ETL pipeline execution.
- Add a data visualisation dashboard.
- Generate sensor monitoring reports.
👩‍💻 Author
Rittika Kundu