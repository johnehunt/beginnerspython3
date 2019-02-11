import pymysql

# Open database connection
connection = pymysql.connect('localhost', 'user', 'password', 'uni-database')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

try:
    # Execute UPDATE command
    cursor.execute("UPDATE students SET email = 'denise@my.com' WHERE id = 7")

    # Commit the changes to the database
    connection.commit()
except:
    # rollback the changes if an exception / error
    connection.rollback()

# Close the database connection
connection.close()
