message = 'hello world'

print(len(message))
# print cha at index 0
print(message[0])
# print hello word only
print(message[:5])
# slicing
print(message[6:])
# replacement
print(message.replace('world','guys'))
# message variable won't change after replace code
print(message)
name = 'ahmed'
# using format function to add strings together
message = '{} , {}. welcome!'.format(name, message)
print(message)
# Lists
courses = ['history', 'Math', 'physics']
courses.append('Art')
print(courses[:1])
courses.insert(0,'Art')
print(courses)
popped = courses.pop()
print(popped ,courses)

# for loop using in
for item in courses:
    print(item )
# index & value of items using in with enumerate()
for index , item in enumerate(courses):
    print(index, item)

list_str = ' - '.join(courses)
new_list = list_str.split(' - ')
print(list_str)
print(new_list)