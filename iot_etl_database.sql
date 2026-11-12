CREATE DATABASE iot_etl_db;
USE iot_etl_db;

CREATE TABLE sensor_readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id VARCHAR(20),
    temperature FLOAT,
    humidity FLOAT,
    location VARCHAR(50)
);
SELECT COUNT(*) FROM sensor_readings;
SELECT * FROM sensor_readings;
TRUNCATE TABLE sensor_readings;