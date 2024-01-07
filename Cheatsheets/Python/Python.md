### **Python Cheat Sheet:**

**1. Basics:**
   - **Printing:**
     - Display information to the console.
     ```python
     print("Hello, Python!")
     ```
   - **Taking Inputs:**
     - Receive user input.
     ```python
     user_input = input("Enter something: ")
     ```

**2. Control Flow:**
   - **For Loops (Various Usages):**
     - Iterate over a sequence or use `range()` for a numerical loop.
     ```python
     for item in iterable:
         # code block

     for i in range(5):
         # code block
     ```

**3. String Manipulation:**
   - **String Formatting:**
     - Combine variables and strings.
     ```python
     name = "John"
     age = 25
     formatted_string = f"My name is {name} and I'm {age} years old."
     ```
   - **String Methods:**
     - Perform various operations on strings.
     ```python
     my_string = "Hello, Python!"

     # Uppercase and lowercase
     upper_case = my_string.upper()
     lower_case = my_string.lower()

     # String length
     length = len(my_string)

     # String concatenation
     new_string = my_string + " Welcome!"

     # String slicing
     sliced_string = my_string[7:12]

     # Check if a substring exists
     is_present = "Python" in my_string
     ```

**4. List Operations:**
   - **List Methods:**
     - Manipulate and modify lists.
     ```python
     my_list = [1, 2, 3, 4, 5]

     # Append and extend
     my_list.append(6)
     my_list.extend([7, 8])

     # Remove and pop
     my_list.remove(3)
     popped_item = my_list.pop()

     # Index and count
     index_of_2 = my_list.index(2)
     occurrences_of_5 = my_list.count(5)

     # Sorting
     my_list.sort()
     reversed_list = sorted(my_list, reverse=True)
     ```

**5. File Handling:**
   - **Reading from a File:**
     ```python
     with open('file.txt', 'r') as file:
         content = file.read()
     ```
   - **Writing to a File:**
     ```python
     with open('new_file.txt', 'w') as file:
         file.write('Hello, Python!')
     ```

**6. Exception Handling:**
   - **Try-Except Blocks:**
     ```python
     try:
         # code block
     except SomeError as error:
         # handle error
     else:
         # code block to execute if no exception
     finally:
         # code block to execute regardless of exceptions
     ```

**7. Classes and Objects:**
   - **Class Definition:**
     ```python
     class MyClass:
         def __init__(self, attribute):
             self.attribute = attribute

         def method(self):
             # code block
     ```
   - **Object Instantiation:**
     ```python
     my_object = MyClass("value")
     ```

**8. Modules and Packages:**
   - **Creating a Module:**
     ```python
     # module.py
     def my_function():
         # code block
     ```
   - **Importing:**
     ```python
     import module
     from module import my_function
     ```

**9. Virtual Environments:**
   - **Creating:**
     ```bash
     python -m venv myenv
     ```
   - **Activating:**
     - Activate virtual environment.
     - Windows: `myenv\Scripts\activate`
     - macOS/Linux: `source myenv/bin/activate`

**10. Regular Expressions:**
   - **Pattern Matching:**
     ```python
     import re
     pattern = re.compile(r'\d+')
     result = pattern.match('123')
     ```

**11. List Comprehensions:**
   ```python
   squares = [x**2 for x in range(10)]
   ```

**12. Decorators:**
   ```python
   def my_decorator(func):
       def wrapper():
           print("Before function call.")
           func()
           print("After function call.")
       return wrapper

   @my_decorator
   def say_hello():
       print("Hello!")
   ```

**13. Generators:**
   ```python
   def my_generator():
       for i in range(5):
           yield i
   ```

**14. Context Managers:**
   ```python
   with open('file.txt', 'r') as file:
       content = file.read()
   ```

**15. Threading and Multiprocessing:**
   - **Threading:**
     ```python
     import threading
     my_thread = threading.Thread(target=my_function)
     my_thread.start()
     ```
   - **Multiprocessing:**
     ```python
     import multiprocessing
     my_process = multiprocessing.Process(target=my_function)
     my_process.start()
     ```

