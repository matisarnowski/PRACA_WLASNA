"""Import module to connect to the database"""
import sqlite3

# Function to connect to the database. Name of the database is data.db
connect = sqlite3.connect("data.db")

connect.execute(
    """CREATE TABLE CUSTOMER
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL);"""
)
# Close the connection
connect.close()
