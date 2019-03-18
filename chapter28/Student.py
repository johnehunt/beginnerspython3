class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        print('__getattr__: ', attribute)
        return 'default'
        # return self.my_default

    # Method will always be called when an attribute is set
    def __setattr__(self, name, value):
        print('__setattr__:', name, value)
        object.__setattr__(self, name, value)

    # Method will always be called when an attribute
    # is accessed, will only called __getattr__ if it
    # does so explicitly or if an AttributeError is raised
    def __getattribute__(self, name):
        print('__getattribute__()', name)
        return object.__getattribute__(self, name)

    def my_default(self):
        return 'default'


student = Student('Katie')

print('Student.__dict__:', Student.__dict__) # Class attribute dictionary
print('student.__dict__:', student.__dict__) # Instance / Object attribute doctionary

print('Student.count:', Student.count)  # class lookup
print('student.name:', student.name)  # instance lookup
print('student.count:', student.count)  # instance lookup finds class attribute

# class lookup
print('Student.count:', Student.count)
print("Student.__dict__['count']:", Student.__dict__['count'])

# Instance / Object Lookup
print('student.name:', student.name)
print("student.__dict__['name']:", student.__dict__['name'])

student.name = 'Bob'
print('student.name:', student.name)  # instance lookup

res1 = student.dummy_attribute
print('student.dummy_attribute:', res1)

student.my_default()

# res2 = student.dummy_method()
# print('student.dummy_method():', res2)

# Attempt to look up class variable via object
# print('student.name:', student.name)
# print("student.__dict__['count']:", student.__dict__['count'])
