# dictionaries
student = {'name':'mohamed', 'age':21, 'courses':['Math','CompSci']}
print(student['courses'])
# add new value or update existing one to  distionary
student['phone'] = '555-5555'
student.update({'name':'mohamed ahmed', 'age':23})
del student['age']
print(student)

# len(student) >> return keys num
# student.keys() >> return keys names
# student.values() >> return only values
# student.items() >> return keys & values
for key , value in student.items():
    print(key, value)

name = input('give me your name: ')
print(name)