'''
Count total vowels in a string using for loop.
'''
count=0
string=input('Enter the String u would like to count vowels of : ')
for char in string:
    if char in 'aeiouAEIOU':
        count += 1
print(f"Total Vowels in the string is {count}")