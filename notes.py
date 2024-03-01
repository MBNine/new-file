# Original Code:

# Displaying a note
print("hello this is notes file for python commands that i'll show throughout the code")

# Integer Command
x = int(3)
print("that is an int command")
print(x)

# Float Command
y = float(3)
print("that is a float command")
print(y)

# Boolean Command
print("that is a boolean command")
print(True)

# String Command
print("that is a string command")
print("this is a string")

# List Command
print("that is a list command")
print([1,2,3])

# Dictionary Command
print("that is a dictionary command")
print({1:2,3:4})

# Tuple Command
print("that is a tuple command")
print((1,2,3))

# Set Command
print("that is a set command")
print({1,2,3})

# Range Command
print("that is a range command")
print(range(10))

# Enumerate Command
print("that is a enumerate command")
print(enumerate([1,2,3]))

# Zip Command
print("that is a zip command")
print(zip([1,2,3],[4,5,6]))

# Conditional Statements
x = 1
if x == 1:
    print("this is an if command")
elif x == 2:
    print("this is an elif command")
else:
    print("this is an else command")

# For Loop
print("that is a for command")
for i in [1,2,3]:
    print(i)

# While Loop
print("that is a while command")
while True:
    print("this is a while command")
    break


# New Code with Explanations:

# Function Definition:
# Defining a function to greet a person
def greet(name):
    print("Hello, " + name + "!")
# Calling the function to greet Alice
greet("Alice")

# List Comprehension:
# Creating a list containing squares of numbers from 0 to 4
squares = [x**2 for x in range(5)]
print("List comprehension - Squares of numbers from 0 to 4:", squares)

# Define a lambda function
# Lambda functions, also known as anonymous functions, are small, inline functions that can be defined without a name.
# They are defined using the lambda keyword, followed by the parameters and a single expression.

# Syntax:
# lambda parameters: expression

# Example:
# Let's define a lambda function that takes two parameters and returns their sum.

sum_lambda = lambda x, y: x + y

# Now, 'sum_lambda' is a lambda function that takes two parameters 'x' and 'y',
# and returns their sum without explicitly defining a function name.

# Using lambda functions:
# Lambda functions can be used in various contexts, such as with higher-order functions like map(), filter(), and reduce(),
# or as inline functions within other functions.

# Example:
# Let's use the 'sum_lambda' function to calculate the sum of two numbers.

result = sum_lambda(3, 5)

# 'result' will now hold the value 8, which is the sum of 3 and 5 calculated using the lambda function.

# Lambda functions are particularly useful in situations where you need a simple, short-lived function without defining a separate named function.


# Import Statement:
# Importing the math module to perform mathematical operations
import math
print("Import statement - Square root of 16:", math.sqrt(16))

# Define a class
# Classes are blueprints for creating objects in object-oriented programming (OOP). 
# They contain properties (attributes) and methods (functions) that define the behavior of the objects.

# Syntax:
# class ClassName:
#     def __init__(self, parameters):  # Constructor method
#         self.attribute = value        # Define attributes
#
#     def method_name(self, parameters): # Define methods
#         # Method body

# Example:
# Let's define a class named 'Car' to represent cars.

class Car:
    def __init__(self, brand, model, year): # Constructor method
        self.brand = brand    # Define attributes
        self.model = model
        self.year = year
        self.running = False  # Additional attribute to track if the car is running

    def start(self):  # Method to start the car
        if not self.running:
            print(f"Starting the {self.brand} {self.model}")
            self.running = True
        else:
            print(f"The {self.brand} {self.model} is already running.")

    def stop(self):   # Method to stop the car
        if self.running:
            print(f"Stopping the {self.brand} {self.model}")
            self.running = False
        else:
            print(f"The {self.brand} {self.model} is already stopped.")

# Creating objects (instances) of the class:
# Objects are instances of a class, created using the class name followed by parentheses.

# Example:
# Let's create two car objects.

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Accessing attributes and calling methods:
# Attributes and methods of objects can be accessed using the dot notation.

# Example:
# Let's access the attributes and call the methods of car1.

print(f"{car1.brand} {car1.model} - Year: {car1.year}")
car1.start()
car1.stop()


# Functions
# Adding numbers function
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Result of addition:", result)
# Of course! In Python, a class serves as a blueprint for creating objects with specific properties and behaviors. 
# In the given class definition, `Dog` is created as a class representing dogs. Within the class, there are two main components: the constructor (`__init__` method) and a method (`bark` method). 
# The constructor initializes each instance of the class with a `name` attribute, which can be provided when creating a new `Dog` object. The `bark` method represents a behavior associated with dogs, in this case, emitting a bark sound along with the dog's name. 
# Within the class, the `self` parameter is used to refer to the current instance of the object, allowing access to its attributes and methods. Instances of the `Dog` class can be created by calling the class like a function, passing any required parameters to the constructor. 
# These instances can then access the class's methods to perform specific actions or behaviors associated with dogs, such as barking. Overall, classes provide a powerful mechanism for organizing and modeling data in Python, allowing for the creation of custom types with well-defined properties and behaviors.
# Define an array
# Arrays are data structures used to store multiple elements of the same data type in contiguous memory locations.

# Syntax:
# In Python, arrays can be defined using lists, which are a built-in data type.

# Example:
# Let's define an array named 'numbers' containing integers.

numbers = [1, 2, 3, 4, 5]

# Here, 'numbers' is an array containing integers 1, 2, 3, 4, and 5.

# Accessing elements:
# Elements in an array can be accessed using their index.

# Example:
# Let's access the first element of the 'numbers' array.

first_element = numbers[0]

# 'first_element' will now hold the value 1, which is the first element of the 'numbers' array.

# Modifying elements:
# Elements in an array can be modified by assigning new values to them using their index.

# Example:
# Let's modify the second element of the 'numbers' array to be 10.

numbers[1] = 10

# Now, the 'numbers' array will be [1, 10, 3, 4, 5].

# Array length:
# The length of an array can be determined using the len() function.

# Example:
# Let's find the length of the 'numbers' array.

array_length = len(numbers)

# 'array_length' will now hold the value 5, which is the length of the 'numbers' array.

#this is try command it tries a code unless there is a value error so it makes another code
try:
    print("hi")
except ValueError:
    print("This is not a number")

#this is an if statement with in to check if a variable is equal to one of the given values.
nos = 2
nos2 = [1, 2, 3, 4, 5]
if nos in nos2:
    print("yes")

#this is an function with attribute (is_integer) to check if it is an integer
x = float(2)
if x.is_integer() == True:
    print("yes")



