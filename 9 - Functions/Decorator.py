'''
Decorator in Python
===================

A decorator is a function that adds extra functionality to another function without modifying its original code.

Think of it like putting a wrapper around a gift:

- Gift = Original function
- Wrapper = Decorator

--------------------------------------------------

Without Decorator

def greet():
    print("Hello Sam")

greet()

Output:
Hello Sam

--------------------------------------------------

Suppose you want to print messages before and after greet():

def greet():
    print("Hello Sam")

print("Before")
greet()
print("After")

Output:
Before
Hello Sam
After

Instead of writing this repeatedly, we use a decorator.

--------------------------------------------------

Why Use Decorators?

Common uses:

1. Logging
2. Authentication/Login Checks
3. Measuring Execution Time
4. Access Control
5. Caching
6. Debugging

--------------------------------------------------

Key Point

A decorator is a function that takes another function,
adds some extra behavior, and returns the modified function.
'''

def decFunc(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper
@decFunc
def greet():
    print("Hello SAM")
greet()
