import pymysql

# Open database connection
connection = pymysql.connect('localhost', 'user', 'password', 'uni-database')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

try:
    # Execute INSERT command
    cursor.execute(
        "INSERT INTO students (id, name, surname, subject, email) VALUES (7, 'Denise', 'Byrne', 'History', 'db@my.com')")
    # Commit the changes to the database
    connection.commit()
except:
    # Something went wrong
    # rollback the changes
    connection.rollback()

# Close the database connection
connection.close()
