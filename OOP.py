# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print('hello my name is ' + self.name)
#
#
# P1 = Person('moham', 22)
# P1.myfunc()
# P1.name = 'mox' # Modify Object property
# P1.myfunc()
# del P1.age # Delete object property
# del P1 # Delete object
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(self.first_name, self.last_name)


x = Person('mohamed', 'anwar')
x.print_name()


class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)  # inherite __init__() from Person class
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome_msg(self):
        print("Welcome", self.first_name, self.last_name, 'To the Class of', self.graduationyear)


x = Student('Muhammad', 'Ahmed', 2020)
x.welcome_msg()
