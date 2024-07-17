import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

def connect_to_mysql_and_load_data():
    try:
        # Read credentials from environment variables
        host = os.getenv('host')
        user = os.getenv('user')
        password = os.getenv('password')
        db = os.getenv('db')
        table_name = os.getenv('table')

        # Connect to MySQL
        connection = mysql.connector.connect(host=host, user=user, password=password, db=db)

        # Create a cursor
        cursor = connection.cursor()

        # Execute a query
        cursor.execute(f"SELECT * FROM {table_name}")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Get the column names
        column_names = cursor.column_names

        # Create a pandas DataFrame
        df = pd.DataFrame(rows, columns=column_names)

        # Print the top 5 rows
        print(df.head())

        # Print data extraction successful
        print("Data extraction successful")

        # Store the DataFrame as a CSV file
        df.to_csv('data.csv', index=False)

    except Error as e:
        print(f"Error while connecting to MySQL: {str(e)}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function
connect_to_mysql_and_load_data()