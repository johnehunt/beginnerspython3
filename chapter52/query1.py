import pymysql


class Student:
    def __init__(self, id, name, surname, subject, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.subject = subject
        self.email = email

    def __str__(self):
        return 'Student[' + str(id) + '] ' + name + ' ' + surname + ' - ' + subject + ' ' + email


# Open database connection
connection = pymysql.connect('localhost', 'user', 'password', 'uni-database')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute('SELECT * FROM students')

print('cursor.rowcount', cursor.rowcount)
print('cursor.description', cursor.description)

# Fetch all the rows and then iterate over the data
data = cursor.fetchall()
for row in data:
    print('row:', row)

# Convert data into Student objects
for row in data:
    student_id, name, surname, subject, email = row
    student = Student(student_id, name, surname, subject, email)
    print(student)

# disconnect from server
connection.close()
