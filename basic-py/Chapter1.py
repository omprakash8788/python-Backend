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







