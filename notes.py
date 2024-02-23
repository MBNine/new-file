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

# Lambda Function:
# Defining a lambda function to add two numbers
add = lambda a, b: a + b
print("Lambda function - Addition result:", add(3, 5))

# Import Statement:
# Importing the math module to perform mathematical operations
import math
print("Import statement - Square root of 16:", math.sqrt(16))

# Class Definition:
# Defining a class representing a Dog with a name and a bark method
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name + " says woof!")
# Creating an instance of the Dog class and using it
dog = Dog("Buddy")
print("Class definition - Dog's name:", dog.name)
dog.bark()

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