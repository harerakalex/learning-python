from first import Person
from functions import bmi, binary_search, search_using_in
# import myturtle

# Creating object from Person 
new_person = Person("gringo", 29)

print('Person name', new_person.name)
print('Person age', new_person.age)

# BMI Calculation
# weight = int(input('Enter your weight: '))
# height = float(input('Enter your height: '))

# print('Your BMI is ', bmi(weight, height))

# Binary Search
array = [20, 2,3,5,1, 4, 8, 19]
array2 = [20, 30, 40]
string_list = ['apple', 'mango', 'Orange', 'Banana']
x = 20

# Some array methods
array.insert(3, 10)
array.append(18)
array.extend(array2)
# array.sort()
array.remove(20)

print('is ',x, 'found in our array ', array, '? ', binary_search(array, x))
print('is ',x, 'found in our array using in keyword ', array, '? ', search_using_in(array, x))

# List comprehension
new_list = [x for x in array if x > 20]

print('New List comprehended ', new_list)

# String Array
string_list = ['apple', 'mango', 'orange', 'banana']
# string_list.sort()

print('String Array', string_list)

help(bmi)
print(16.0 // 4)
print(type(3.3))

# Deal with strings
mystr = 'hello gringo'

print('sub str', mystr[-1])
print(mystr.count("e"))