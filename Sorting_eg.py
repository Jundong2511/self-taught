# compare .sort() and sorted()

list = [3,78,89,6,5,3,2,5,7,9,9]

sorted_list = sorted(list)
list.sort() # nothing return
print(list == sorted_list)
# this return True

tup = (3,78,89,6,5,3,2,5,7,9,9)
### tup.sort() # this is not working, tuple dosen't have .sort() function
# tuple only can user sorted(), but it return a list.
sorted_tup = sorted(tup)
print sorted_tup

# dictionary only can be sort keys, this return a list of keys, not include values.
dict = {'name':'Jun', 'job':'Sushi Chef', 'age': '30', 'os':'Mac'}
sorted_dict = sorted(dict)
print sorted_dict
# output ['age', 'job', 'name', 'os']


# when sort a list of numbers, can add key parameter to sort by key, e.g. key=abs
#  e.g. key=abs, this will sort by abuslote numer.
list = [-6, -5, -4,1,2,3]
sorted_list = sorted(list, key=abs)
print(sorted_list)
# output [1, 2, 3, -4, -5, -6]


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 28, 80000)
e2 = Employee('July', 32, 40000)
e3 = Employee('Tim', 55, 90000)

employees = [e1,e2,e3]
