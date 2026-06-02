'''
parameter is placeholder for the value in function
argument is a value that we want to pass
'''

def greeting(name): #name is a parameter here
    print ('Hi', name)
greeting('Saaiem') # Saaiem is an Argument here
greeting('Tanishka')

'''Eg. 2'''
def sum(a, b):
    print(f"Summation of two digit is : " ,a+b)
sum(2, 4)

'''
Types of Arguments: There are 3 types of arguments,
1. Positional Argument 
2. Keyword Argument
3. default Argument
'''

# This is positional argument where we have to give data in the input at same position as defined
def myself(name, age):
    print(f'Hi my Name is {name} and i am {age} years old') 

myself('Saaiem Salaar', 22)
myself(22, 'Saaiem Salaar') #wrong

#Key word argument is when u directly define the values in Function callling, using this eliminates the positional argument disadvantage
def myself(name, age):
    print(f'Hi my Name is {name} and i am {age} years old') 

myself(age=22, name='Saaiem Salaar')

# default argument is when we assign a default value to the parameter, if we don't pass any value then it will take default value
def myself(name='john doe', age=22):
    print(f'Hi my Name is {name} and i am {age} years old')
myself() # it will take default value
myself('Saaiem Salaar', 26) # it will take the value that we have passed in function calling, it will not take default value because we have passed the value in function calling