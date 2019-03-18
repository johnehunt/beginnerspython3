
# Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

# Output the basic sets
print('exam:', exam)
print('project:', project)

# Students taking both exam and project
print(exam & project)

# Only took the exam
print(exam - project)

# Only took the project
print(project - exam)

# All students
print(exam | project)

# Students who took the exam or the project but not both
print(exam ^ project)