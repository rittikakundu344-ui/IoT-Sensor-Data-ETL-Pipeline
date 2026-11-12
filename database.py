
import mysql.connector

def create_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="iot_etl_db"
    )

    return conn




def load_data(data):

    conn = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO sensor_readings
    (sensor_id, temperature, humidity, location)
    VALUES (%s, %s, %s, %s)
    """

    values = [
        (
            row["sensor_id"],
            row["temperature"],
            row["humidity"],
            row["location"]
        )
        for row in data
    ]

    cursor.executemany(query, values)

    conn.commit()

    print("Data loading completed!")
    print("New records inserted:", cursor.rowcount)

    cursor.close()
    conn.close()
