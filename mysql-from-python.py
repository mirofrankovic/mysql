import os
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
        list_of_names = ['Bianka', 'bianka']
        #Prepare a list with the same number of placeholders as a list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        rows = cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()