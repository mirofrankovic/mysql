import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("""Create Table if not exists
                        Friends(name char(20), age int, DOB datetime); """)
       # Note that the above will still display a error (not error) if the table
       # olready exists
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()