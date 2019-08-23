user = 'Admin'
logged_in = False

# or
# and
# not

if not logged_in:
    print('please log in')
else:
    print('welcome')

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)