'''
reverse a string using for loop.
'''
reverse=""
string=input('Enter the String u would like to Reverse: ')
for char in string:
    reverse = char + reverse
    #print(reverse) #uncomment to see simulation of how it works
print(f"reversed string is '{reverse}'")