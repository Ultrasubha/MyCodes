# Understanding SOLID Principles in Object-Oriented Design

## Introduction

Object-oriented design principles play a crucial role in creating maintainable, scalable, and flexible software systems. The SOLID principles, introduced by Robert C. Martin, provide a set of guidelines to achieve these goals. <br>

These five SOLID principles are: 

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

## Single Responsibility Principle (SRP)

The SRP states that a class should have only one reason to change, meaning it should have only one responsibility. This promotes modular and maintainable code.

**Example in Python:**

```python
class FileManager:
    def read_file(self, file_path):
        # Read file implementation

    def write_file(self, file_path, content):
        # Write file implementation
```
## Open/Closed Principle (OCP)

The OCP encourages classes to be open for extension but closed for modification. This is achieved through the use of interfaces and abstract classes.

**Example in Python:**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
```

## Liskov Substitution Principle (LSP)
The LSP states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. This ensures that inheritance is used appropriately.

**Example in Python:**
```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def swim(self):
        print("Penguin swimming")
```

## Interface Segregation Principle (ISP)
The ISP advises that a class should not be forced to implement interfaces it does not use. This prevents the creation of large, monolithic interfaces.

**Example in Python:**

```python
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Engineer(Worker):
    def work(self):
        print("Engineering work")

    def eat(self):
        print("Eating lunch")
```

## Dependency Inversion Principle (DIP)
The DIP suggests that high-level modules should not depend on low-level modules but both should depend on abstractions. This promotes the use of dependency injection.

**Example in Python:**

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb turned on")

    def turn_off(self):
        print("LightBulb turned off")

class Switchable:
    def operate(self):
        pass

class Switch(Switchable):
    def __init__(self, device):
        self.device = device

    def operate(self):
        # Some operations before turning on/off
        self.device.turn_on()
```

## Conclusion
By adhering to the SOLID principles, developers can create more maintainable, extensible, and robust software systems. These principles guide the design process and contribute to the overall quality and longevity of the codebase.