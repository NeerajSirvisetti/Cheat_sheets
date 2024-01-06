

### **Python Basics:**
```python
# Variables and Data Types
x = 5
name = "John"
float_num = 3.14
boolean_val = True

# Lists
my_list = [1, 2, 3, "apple", "banana"]
my_list.append(4)
element = my_list[2]

# Tuples
my_tuple = (1, 2, 3)

# Dictionaries
my_dict = {"key1": "value1", "key2": 42}
value = my_dict["key1"]

# Strings
string_val = "Hello, World!"
substring = string_val[7:12]

# Input/Output
user_input = input("Enter something: ")
print("You entered:", user_input)
```

### **Control Flow:**
```python
# Conditional Statements
if condition:
    # code to execute if the condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if no conditions are True

# Loops
for item in my_list:
    # code to execute for each item in the list

while condition:
    # code to execute while the condition is True
```

### **Functions:**
```python
# Function Definition
def greet(name):
    return "Hello, " + name

# Function Call
result = greet("Alice")
```

### **File Handling:**
```python
# Reading from a file
with open("filename.txt", "r") as file:
    content = file.read()

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, File!")
```

### **Classes and Objects:**
```python
# Class Definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

# Object Instantiation
person1 = Person("Alice", 25)
```

### **Exception Handling:**
```python
try:
    # code that might raise an exception
except SomeException as e:
    # handle the exception
else:
    # code to execute if no exception occurred
finally:
    # code that always runs, regardless of exceptions
```
