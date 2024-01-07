### **Classes and Objects Concepts:**

**1. Classes:**
   - **Definition:** A class is a blueprint for creating objects. It defines attributes and methods that the objects of the class will have.
   - **Example:**
     ```python
     class Car:
         def __init__(self, make, model):
             self.make = make
             self.model = model

         def display_info(self):
             print(f"{self.make} {self.model}")
     ```
   **Explanation:** The `Car` class has attributes (`make` and `model`) and a method (`display_info`) to display information about the car.

**2. Objects:**
   - **Definition:** An object is an instance of a class. It represents a concrete entity created from the class blueprint.
   - **Example:**
     ```python
     my_car = Car("Toyota", "Camry")
     my_car.display_info()
     ```
   **Explanation:** `my_car` is an object created from the `Car` class. It has the attributes "Toyota" and "Camry" and can call the `display_info` method.

**3. Inheritance:**
   - **Definition:** Inheritance allows a class to inherit attributes and methods from another class. It promotes code reusability and helps create a hierarchy of classes.
   - **Example:**
     ```python
     class ElectricCar(Car):
         def __init__(self, make, model, battery_capacity):
             super().__init__(make, model)
             self.battery_capacity = battery_capacity

         def display_info(self):
             print(f"{self.make} {self.model} (Electric)")
     ```
   **Explanation:** The `ElectricCar` class inherits from `Car` and adds a new attribute (`battery_capacity`) and overrides the `display_info` method.

### **Classes and Objects Cheat Sheet:**

**1. Define a Class with Constructor (`__init__`):**
```python
class MyClass:
    class_variable = "Class Variable"

    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method(self):
        print("Class method")
```
**Explanation:** Creates a class with a class variable, attributes, and a method. The `__init__` method is the constructor, initializing object attributes.

---

**2. Access Class Variable:**
```python
print(MyClass.class_variable)
```
**Explanation:** Accesses the class variable without creating an object.

---

**3. Dunder Methods (`__str__` and `__add__`):**
```python
class DunderClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"DunderClass instance with value: {self.value}"

    def __add__(self, other):
        return DunderClass(self.value + other.value)
```
**Explanation:** Defines dunder methods for string representation (`__str__`) and addition (`__add__`).

---

**4. Use of `self`:**
```python
def method(self):
    print(f"Accessing attribute: {self.attribute1}")
```
**Explanation:** `self` refers to the instance of the object. It is used to access object attributes and methods within the class.

---

**5. Class and Static Methods:**
```python
class MethodClass:
    class_variable = "Class Variable"

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print(f"Instance method with value: {self.value}")

    @classmethod
    def class_method(cls):
        print(f"Class method with class variable: {cls.class_variable}")

    @staticmethod
    def static_method():
        print("Static method")
```
**Explanation:** Defines instance, class, and static methods.

---

**6. Getter and Setter Methods:**
```python
class GetterSetterClass:
    def __init__(self):
        self._value = 0

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if new_value >= 0:
            self._value = new_value
```
**Explanation:** Defines methods (`get_value` and `set_value`) for getting and setting private attribute values.

---

**7. Property Decorator:**
```python
class PropertyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
```
**Explanation:** Uses `@property` to create a read-only property and `@property_name.setter` to create a property with a setter.

---

**8. Inheritance and Super:**
```python
class BaseClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

class DerivedClass(BaseClass):
    def __init__(self, attribute1, attribute2, new_attribute):
        super().__init__(attribute1, attribute2)
        self.new_attribute = new_attribute

    def new_method(self):
        print("New method")
```
**Explanation:** Defines a base class (`BaseClass`) and a derived class (`DerivedClass`) with inheritance using `super()`.

---
The provided cheat sheet covers a comprehensive set of concepts for classes and objects in Python. It includes the following key concepts:

1. **Class Definition and Constructor (`__init__`):** How to define a class with attributes and a constructor to initialize object properties.

2. **Accessing Class Variables:** Demonstrates accessing class variables without creating an object.

3. **Dunder Methods (`__str__` and `__add__`):** Introduces dunder methods for string representation and addition.

4. **Use of `self`:** Explains the use of `self` within methods to refer to the instance of the object.

5. **Class and Static Methods:** Shows the implementation of instance, class, and static methods.

6. **Getter and Setter Methods:** Illustrates methods for getting and setting private attribute values.

7. **Property Decorator:** Demonstrates the use of the `@property` decorator for read-only properties and `@property_name.setter` for properties with a setter.

8. **Inheritance and Super:** Introduces the concept of inheritance and using `super()` to call the constructor of the parent class.

