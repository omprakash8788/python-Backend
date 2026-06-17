print("Hello")

# Chap2 -> Topic - Variable and Data Types

# Assigning a value to a variable
message = "Hello, world!"
number = 42
pi_value = 3.14

# Printing the value 
print(message, number, pi_value) #I am lazy


# Common data types
# Integers(), Floating Point numbers(), String , Booleans, List, Tuples, Dictionaries

integer =10
floating_point = 10.5
string="Python programming"
boolean=True
list_example=[1,2,3,4]
tuple_example=(1,2,3,4)
dictionary_exmple={"name":"john", "age":40}

# Displaying the data types of each variables
print(type(integer))
print(type(floating_point))
print(type(string))
print(type(boolean))
print(type(list_example))
print(type(tuple_example))
print(type(dictionary_exmple)) #Now i am not lazy

#Type Conversion

# Converting integer to float
num_int=10
nums_float=float(num_int)
print(nums_float)

# Converting  float to integer
nums_float=9.7
num_int=int(nums_float)
print(num_int)

# Converting integer to string
num_int=300
num_str=str(num_int)
print(num_str)

# Converting string to integer

num_str="800"
num_int=int(num_str)
print(num_int)


# Chap -2 (Operators and Expressions)

#Additions
addition= 5 +3
print("additions", addition)

#Sub 
subtraction = 5 - 3
print("sub", subtraction)

#Mutliplication
multiplication = 6 * 6
print("multi", multiplication)

# Division
division = 5/3
print("Division", division)


# Modulus (remainder)
modulus = 5 % 3
print("Modulus:", modulus)

# Exponentiation (power)
exponentiation = 5 ** 3
print("Exponentiation:", exponentiation) 


# Comparison Operators 
# Equal to
equal = 5==3
print(equal) 

# Not equal 
not_equal = 5!=4
print(not_equal)

# Greater than
greater_than = 5 > 3
print("Greater Than:", greater_than)

# Less than
less_than = 5 < 3
print("Less Than:", less_than)


# Greater than or equal to
greater_than_equal = 5 >= 3
print("Greater Than or Equal To:", greater_than_equal)

# Less than or equal to
less_than_equal = 5 <= 3
print("Less Than or Equal To:", less_than_equal)

#  Logical Operators

x = True
y = False

# Logical AND
print("x and y : ", x and y )

# Logical OR
print("x or y : ", x or y )

# Logical NOT
print("not x:", not x) 


# Logical operators often combine multiple comparison operations:
a = 10 
b=12
c=5

# Combining comparison and logical operators

result = (a > b) and (a > c)
print(result)

result =(a > b) or (a > c)
print(result)

result = not(a > b)
print(result)


#Chap -4: Control Structures

# Conditional Statements

age = 20
if age >=18:
    print("You are eligible for vote.")
else:
    print("You are not eligible baby")

# You can also have multiple conditions using :

score = 75
if score >=90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
else:
    print("Grade: D or lower")


# Loops in python 

# For Loops 
#  Iterate over a list
fruits =["apple", "banana", "cherry"]
for fruit in fruits:
    print("Current fruits: ", fruit)


# While Loops
# Using a while loop to count to 5
count =1
while count <=5:
    print("count: ", count)
    count +=1

# Nested Loops and Cnditinal structures
# Nested for loops to iterate over a grid layout
for i in range(1, 4):
    for j in range(1, 4):
        print(f'({i}, {j})', end=' ')
    print()

# Find the first even number in each list
list_of_lists =[[1,3,5], [2,4,6],[9,7,5]]

for sublist in list_of_lists:
    for number in sublist:
        if number % 2==0:
            print("First even number in list :", number)
            break


# Combining Loops and Conditional Statements
# Print number from 1 to 10 , skip number divisible by 3

for i in range(1,10):
    if i % 3==0:
        continue
    print(i)


# Chapter 5 : Functions and Modules 

def greet():
    print("Hello, welcome to python")
# Calling the function
greet()


# Example of a unction with Parameters and a Return value:
def add_numbers(num1, num2):
    result = num1 + num2
    return result
# Calling the function with parameters
sum_result = add_numbers(7,8)
print(sum_result)

# Using Default Parameters and Keyword Arguments:
def describe_pet(pet_name, animal_type='dog'):
 print(f"I have a {animal_type} named {pet_name}.")
# Calling function with default parameter
describe_pet(pet_name='Rex')
# Calling function with both parameters explicitly
describe_pet(pet_name='Whiskers', animal_type='cat')


# Importing modules 

import math
# Using a function from the math module
print("The square root of 16 is:", math.sqrt(16))


# Importing Specific Functions: You can also choose to import
# specific functions from a module:

from math import sqrt, pow
# Now no need to use 'math.' prefix
print("The square root of 25 is:", sqrt(25))
print("2 raised to the power 5 is:", pow(2, 5))


# Chapter 6: Exception Handling

numbers =[1,2,3]
try:
    print(numbers[3])
except IndexError as e:
    print("Error: ", e)


# Handling mutiple exceptions
try:
    value = int(input("Please enter a number: "))
    result = 10 /value
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Result: ", result)
finally:
    print("This block is always excuted")






