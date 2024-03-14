# Data Types
A data type is a classification that specifies which type of value a variable can hold.

```python
# Integer
integer_variable = 42
# Float
float_variable = 3.14
# String
string_variable = "Hello, World!"
# Boolean
boolean_variable = True
# List
list_variable = [1, 2, 3, "four", 5.0]
# Tuple
tuple_variable = (10, "tuple", 3.14)
# Set
set_variable = {1, 2, 3, 3, 4, 5}
# Dictionary
dictionary_variable = {"key1": "value1", "key2": 42, "key3": [1, 2, 3]}

# Print the variables
print("Integer:", integer_variable)
print("Float:", float_variable)
print("String:", string_variable)
print("Boolean:", boolean_variable)
print("List:", list_variable)
print("Tuple:", tuple_variable)
print("Set:", set_variable)
print("Dictionary:", dictionary_variable)
```
# Dictionary
A dictionary is an unordered collection of key-value pairs, where each key must be unique and maps to a specific value.

```python
class MyDictionary:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value):
        self.data[key] = value

    def remove_item(self, key):
        if key in self.data:
            del self.data[key]
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def get_value(self, key):
        return self.data.get(key, None)

    def get_keys(self):
        return list(self.data.keys())

    def get_values(self):
        return list(self.data.values())

    def get_items(self):
        return list(self.data.items())

# Example usage:
my_dict = MyDictionary()

my_dict.add_item("name", "John")
my_dict.add_item("age", 25)
my_dict.add_item("city", "New York")

print("Dictionary:", my_dict.get_items())

my_dict.remove_item("age")
print("After removing 'age':", my_dict.get_items())

print("Value for 'name':", my_dict.get_value("name"))
print("Keys:", my_dict.get_keys())
print("Values:", my_dict.get_values())
```
# Array Methods(List)
## Initialization
```python
# Create list
my_list = []
numbers = [1, 2, 3, 4, 5]
```

## Common Operations
```python
element = numbers[2]            # Access an element by index
numbers.append(6)               # Add an element to the end
numbers.insert(2, 10)           # Insert an element at a specific index
numbers.remove(3)               # Remove an element by value
last_element = numbers.pop()    # Remove and return the last element
index = numbers.index(4)        # Find the index of an element
is_present = 5 in numbers       # Check if an element is in the list
numbers.sort()                  # Sort the list in ascending order
numbers.reverse()               # Reverse the order of the list
```

# String Methods
## Basic Operations
```python
full_string = "Hello" + " " + "World"   # Concatenate strings
repeated_string = "Python" * 3          # Repeat a string
char = full_string[0]                   # Access characters by index
```

## Common Methods
```python
length = len(full_string)                           # Get the length of a string
lowercase_str = full_string.lower()                 # Convert to lowercase
uppercase_str = full_string.upper()                 # Convert to uppercase
starts_with_hello = full_string.startswith("Hello") # Check if a string starts with a prefix
ends_with_world = full_string.endswith("World")     # Check if a string ends with a suffix
new_str = full_string.replace("Hello", "Hi")        # Replace a substring
word_list = full_string.split(" ")                  # Split a string into a list
```

# Decorators
A decorator is a concise way to modify or extend the behavior of functions or methods by wrapping them with additional functionality.

```python
def my_decorator(func):                         # Decorator function
    def wrapper(*args, **kwargs):
        print("Before function execution.")
        result = func(*args, **kwargs)
        print("After function execution.")
        return result
    return wrapper

@my_decorator                                   # Applying the decorator
def my_function(name):
    print(f"Hello, {name}!")

my_function("Alice")                            # Calling the decorated function
```

# Object Oriented Programming System
## Class Definition
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
```
## Object Creation
```python
my_car = Car("Toyota", "Camry", 2022)       # Instantiate an object
```
## Accessing Attributes and Methods
```python
car_make = my_car.make      # Accessing attributes
my_car.display_info()       # Calling methods
```
## Inheritance
```python
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    # Additional methods or overrides can be added
```
## Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")
```
## Polymorphism
```python
class Circle:
    def calculate_area(self, radius):
        return 3.14 * radius ** 2

class Square:
    def calculate_area(self, side):
        return side ** 2

# Both Circle and Square have a method named calculate_area
# Enables code flexibility and reusability
```