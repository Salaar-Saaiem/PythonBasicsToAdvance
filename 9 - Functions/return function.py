"""
return is used to return a value from a function. 
It can be used to return any type of value, including numbers, strings, lists, dictionaries, and even other functions.
"""

def add(a, b):
    return a + b  #here we are returning the sum of a and b
  
result = add(2, 3)
print(result) # Output: 5
print(add(4, 5)) # Output: 9

# if we don't use return statement in function, it will return None by default
def add2(a, b): 
    result = a + b # here we are printing the sum of a and b, but not returning it
result = add2(2, 3)
print(result) # Output: None