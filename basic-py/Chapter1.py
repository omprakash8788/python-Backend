# print("Hello")

# # Chap2 -> Topic - Variable and Data Types

# # Assigning a value to a variable
# message = "Hello, world!"
# number = 42
# pi_value = 3.14

# # Printing the value 
# print(message, number, pi_value) #I am lazy


# # Common data types
# # Integers(), Floating Point numbers(), String , Booleans, List, Tuples, Dictionaries

# integer =10
# floating_point = 10.5
# string="Python programming"
# boolean=True
# list_example=[1,2,3,4]
# tuple_example=(1,2,3,4)
# dictionary_exmple={"name":"john", "age":40}

# # Displaying the data types of each variables
# print(type(integer))
# print(type(floating_point))
# print(type(string))
# print(type(boolean))
# print(type(list_example))
# print(type(tuple_example))
# print(type(dictionary_exmple)) #Now i am not lazy

# #Type Conversion

# # Converting integer to float
# num_int=10
# nums_float=float(num_int)
# print(nums_float)

# # Converting  float to integer
# nums_float=9.7
# num_int=int(nums_float)
# print(num_int)

# # Converting integer to string
# num_int=300
# num_str=str(num_int)
# print(num_str)

# # Converting string to integer

# num_str="800"
# num_int=int(num_str)
# print(num_int)


# # Chap -2 (Operators and Expressions)

# #Additions
# addition= 5 +3
# print("additions", addition)

# #Sub 
# subtraction = 5 - 3
# print("sub", subtraction)

# #Mutliplication
# multiplication = 6 * 6
# print("multi", multiplication)

# # Division
# division = 5/3
# print("Division", division)


# # Modulus (remainder)
# modulus = 5 % 3
# print("Modulus:", modulus)

# # Exponentiation (power)
# exponentiation = 5 ** 3
# print("Exponentiation:", exponentiation) 


# # Comparison Operators 
# # Equal to
# equal = 5==3
# print(equal) 

# # Not equal 
# not_equal = 5!=4
# print(not_equal)

# # Greater than
# greater_than = 5 > 3
# print("Greater Than:", greater_than)

# # Less than
# less_than = 5 < 3
# print("Less Than:", less_than)


# # Greater than or equal to
# greater_than_equal = 5 >= 3
# print("Greater Than or Equal To:", greater_than_equal)

# # Less than or equal to
# less_than_equal = 5 <= 3
# print("Less Than or Equal To:", less_than_equal)

# #  Logical Operators

# x = True
# y = False

# # Logical AND
# print("x and y : ", x and y )

# # Logical OR
# print("x or y : ", x or y )

# # Logical NOT
# print("not x:", not x) 


# # Logical operators often combine multiple comparison operations:
# a = 10 
# b=12
# c=5

# # Combining comparison and logical operators

# result = (a > b) and (a > c)
# print(result)

# result =(a > b) or (a > c)
# print(result)

# result = not(a > b)
# print(result)


# #Chap -4: Control Structures

# # Conditional Statements

# age = 20
# if age >=18:
#     print("You are eligible for vote.")
# else:
#     print("You are not eligible baby")

# # You can also have multiple conditions using :

# score = 75
# if score >=90:
#     print("Grade: A")
# elif score >=80:
#     print("Grade: B")
# elif score >=70:
#     print("Grade: C")
# else:
#     print("Grade: D or lower")


# # Loops in python 

# # For Loops 
# #  Iterate over a list
# fruits =["apple", "banana", "cherry"]
# for fruit in fruits:
#     print("Current fruits: ", fruit)


# # While Loops
# # Using a while loop to count to 5
# count =1
# while count <=5:
#     print("count: ", count)
#     count +=1

# # Nested Loops and Cnditinal structures
# # Nested for loops to iterate over a grid layout
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f'({i}, {j})', end=' ')
#     print()

# # Find the first even number in each list
# list_of_lists =[[1,3,5], [2,4,6],[9,7,5]]

# for sublist in list_of_lists:
#     for number in sublist:
#         if number % 2==0:
#             print("First even number in list :", number)
#             break


# # Combining Loops and Conditional Statements
# # Print number from 1 to 10 , skip number divisible by 3

# for i in range(1,10):
#     if i % 3==0:
#         continue
#     print(i)


# # Chapter 5 : Functions and Modules 

# def greet():
#     print("Hello, welcome to python")
# # Calling the function
# greet()


# # Example of a unction with Parameters and a Return value:
# def add_numbers(num1, num2):
#     result = num1 + num2
#     return result
# # Calling the function with parameters
# sum_result = add_numbers(7,8)
# print(sum_result)

# # Using Default Parameters and Keyword Arguments:
# def describe_pet(pet_name, animal_type='dog'):
#  print(f"I have a {animal_type} named {pet_name}.")
# # Calling function with default parameter
# describe_pet(pet_name='Rex')
# # Calling function with both parameters explicitly
# describe_pet(pet_name='Whiskers', animal_type='cat')


# # Importing modules 

# import math
# # Using a function from the math module
# print("The square root of 16 is:", math.sqrt(16))


# # Importing Specific Functions: You can also choose to import
# # specific functions from a module:

# from math import sqrt, pow
# # Now no need to use 'math.' prefix
# print("The square root of 25 is:", sqrt(25))
# print("2 raised to the power 5 is:", pow(2, 5))


# # Chapter 6: Exception Handling

# numbers =[1,2,3]
# try:
#     print(numbers[3])
# except IndexError as e:
#     print("Error: ", e)


# # Handling mutiple exceptions
# try:
#     value = int(input("Please enter a number: "))
#     result = 10 /value
# except ValueError:
#     print("You must enter a valid integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# else:
#     print("Result: ", result)
# finally:
#     print("This block is always excuted")

# # Raising Excetions 

# def check_age(age):
#     if age < 0 :
#         raise ValueError("Age cannot be negative.")
#     elif age < 18:
#         print("You are not old enough")
#     else:
#         print("You are welcome.")

# try:
#     user_check=int(input("Enter your age: "))
#     check_age(user_check)
# except ValueError as e:
#     print("Error: ", e)

# # Example of a Custom Exception:
# # class NegativeAgeError(Exception):
# #  """Exception raised when the age is negative."""
# #  def __init__(self, age):
# #   self.message = f"Age {age} is not valid. Age cannot be negative."
# #  super().__init__(self.message)

# # def check_age(age):
# #  if age < 0:
# #   raise NegativeAgeError(age)
# #  print(f"Age {age} is valid.")
# # try:
# #  check_age(-5)
# # except NegativeAgeError as e:
# #   print(e)

# # Chap7 - Working with Files 
# # r- reading
# # w- writing
# # a- appending

# # Example of read file
# try:
#    with open('example.txt', 'r') as file:
#       content=file.read()
#       print(content)
# except FileNotFoundError:
#    print("File not found")

# # Example of write file -> Weiting to a file, overwriting existing content
# with open('example.txt', 'w') as file:
#     file.write("Hello")
#     file.write("Writing to files is essential.")

# # Appending to a file without overwriting it 
# with open('example.txt', 'a') as file: 
#     file.write("\nAppending a new line.") 


# # Working with Different File Formats
# import csv

# # Writing to csv file
# with open('example.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Alice", "26"])
#     writer.writerow(["Bob", "12"])

# #Reading from a CSV file 
# with open('example.csv', 'r') as file: 
#     reader = csv.reader(file) 
#     for row in reader: 
#         print(row) 

# Working with JSON Files:

# import json

# data={
#     "name":"op",
#     "age":25,
#     "city":"New York"
# }

# # Writing JSON to a file
# with open('data.json', 'w') as file:
#     json.dump(data, file)


# # Reading JSON from a file
# with open('data.json','r') as file:
#     data=json.load(file)
#     print(data)


# Chapter 8 : Data Structures
# List , tuple , sets, dictionaries

# Example of list
# Creating a list
# fruits =["apples", "banana", "cherry"]
# print(fruits)

# # Adding an element to the end of the list
# fruits.append("orange")
# print("After adding", fruits)

# # Inserting an element at a specific postion
# fruits.insert(1, "blueberry")
# print("After inserting: ", fruits)

# # Removing an element
# fruits.remove("banana")
# print("After removing: ", fruits)

# # Accessing elements
# print("First fruit: ", fruits[0])
# print("Last fruit: ", fruits[-1])


# # Slicing a list
# print("First two fruits: ", fruits[0:3])




# Tuples 
# Tuples are immutable
# Create a tuple
# colors =("red", "green", "blue")
# print("Original tuple:", colors)

# # Accessing tuple elements
# print("First color:", colors[0])

# # Tuples are immutable , so you cannot change their elenents
# # colors[0]="yellow"
# # print(colors) X TypeError: 'tuple' object does not support item assignment


# # Tuples can be used as keys in dictionaries, where lists cannot 
# color_preferences = {colors: "John's favorite colors"} 
# print(color_preferences) 


# Sets

# Creating a set
# numbers={1,2,3,4,4,5}
# print("Original set: ", numbers)

# # Adding an element to a set
# numbers.add(6)
# print("After adding :", numbers)

# # Removing en element
# numbers.remove(1)
# print("After removing: ", numbers)

# # Checking membership
# print("Is 3 in numbers?", 3 in numbers)

# # Operations like union, intersection, difference 
# a = {1, 2, 3} 
# b = {3, 4, 5} 
# print("Union:", a | b) 
# print("Intersection:", a & b) 
# print("Difference:", a - b)


# Dictionaries
# Creating a dictionary 
# person = {"name": "John", "age": 30, "city": "New York"} 
# print("Original dictionary:", person) 
# # Accessing values by key 
# print("Name:", person["name"]) 
# # Adding a new key-value pair 
# person["job"] = "Programmer" 
# print("After adding:", person) 
# # Removing a key-value pair 
# del person["age"] 
# print("After deletion:", person) 
# # Using the get method to avoid KeyError 
# print("Age:", person.get("age", "Not available")) 
# # Iterating over keys and values 
# for key, value in person.items(): 
#     print(key, ":", value) 

# Chapter 9 - Object - Oriented Programming

# class Dog:
#     # Class attribute
#     species ="Canis familiaris"
#     # Initializer / Instance attributes
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

# # creating an object
# my_dog=Dog("Buddy", 6)
# # Accessing the obj
# print(f"My dog {my_dog.name} is {my_dog.age} years old and belongs to the species {my_dog.species}.") 


# Chapter 10 -  Libraries and Frameworks
# Popular Python Libraries
# 1. NumPy 

# import numpy as np
# a = np.array([1,2,3])
# print("Array: ",a)
# print("Mean of array:", np.mean(a))

# 2.  Pandas 
# import pandas as pd
# data={'Name': ['John', 'Anna', 'James'], 'Age': [28, 24,35]} 
# df=pd.DataFrame(data)
# print(df)

# 3. 3. Matplotlib : A plotting library for creating static, animated, and interactive visualizations in Python

# import matplotlib.pyplot as plt 
# plt.plot([1, 2, 3, 4]) 
# plt.ylabel('Example Numbers') 
# plt.show() 

# 4. Scikit-learn : A tool for data mining and data analysis. It is
# built on NumPy, SciPy, and Matplotlib and is widely used for
# machine learning applications.


# from sklearn.ensemble import RandomForestClassifier 
# clf = RandomForestClassifier(random_state=0) 
# X = [[1, 2, 3], [11, 12, 13]]  # Two samples, three features 
# y = [0, 1]  # Classes of each sample 
# clf.fit(X, y) 

# Introduction to Frameworks
# 1. Django
# 2. Flash

# Chapter 11: Debugging and Testing

# def calculate_sum(numbers): 
#     total = 0 
#     for number in numbers: 
#         total += number 
#         print(f"Added {number}, total now {total}")  # Debug
#         print
#         return total 

# print(calculate_sum([1, 2, 3, 4])) 


# Chapter 13: Data Analysis with Python





