"""Greets the user"""
def greet(name):
    print(f"Hello, {name}!")    

greet("World")

"""Adds a and b and returns a result."""
def add(a, b):
    return a + b

print(f"ADD: {add(6, 7)}")  # This line will never be executed because it's after the return statement  

def subtract(a, b):
    return a - b

print(f"SUBTRACT: {subtract(6, 7)}")