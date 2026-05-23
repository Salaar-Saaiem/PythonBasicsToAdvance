"""
Data Types are the values u put inside the variables
it can be 

NUMERIC DATA TYPES:
int : integer- 100 200 300 -4000
float: decimal nummbers- 2.3 21.3

BOOLEAN DATATYPES
these data types are used in logical operations where output must be, TRUE or FALSE, YES or NO, O or 1

if you want to know which type of data type, a variable is using, use type() function
"""

name= 'SAM' # String Data Type
age = 21 # Intereger Data Type
height=185.2 # Float Data Type
bloodgrp = 'A+' # String Data Type
is_disabled= False

print("Name:",name, "\nAge:",age, "Height:", height, "\nBlood Group:", bloodgrp, "\nDisability:", is_disabled)

print(type(name), type(age),type(height),  type(bloodgrp))

