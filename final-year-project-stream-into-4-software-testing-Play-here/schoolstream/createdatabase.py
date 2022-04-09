#Python Script to Create the Database
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    passwd = ""
    )

my_cursor = mydb.cursor()

# Execute Only once to create the database
my_cursor.execute("CREATE DATABASE school_stream_testing")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)


