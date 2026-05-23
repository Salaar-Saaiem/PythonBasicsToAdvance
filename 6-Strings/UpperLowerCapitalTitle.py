'''
if the user entered all the charaters in upper or mixed, but our code is written for handling lower cases
we can use,
.upper() -> Convert all charater of the string into upper case
.lower() -> Convert all charater of the string into lower case
.capitalize() -> it capitalize first charater of the string only
.title() -> it capitalize first charater of each word in the string 
functions
'''
# Either we can use it during printing
name='saAiem saLaar'
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())

# Or we can convert it during taking input
name2=input('Enter Your Name: ').lower()
print(name2)
name3=input('Enter Your Name: ').upper()
print(name3)
name4=input('Enter Your Name: ').capitalize()
print(name4)
name5=input('Enter Your Name: ').title()
print(name5)