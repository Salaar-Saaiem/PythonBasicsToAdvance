'''
if the user entered all the charaters in upper or mixed, but our code is written for handling lower cases
we can use,
.upper()
.lower()
functions
'''
# Either we can use it during printing
name='Saaiem Salaar'
print(name.lower())
print(name.upper())

# Or we can convert it during taking input
name2=input('Enter Your Name: ').lower()
print(name2)
name3=input('Enter Your Name: ').upper()
print(name3)