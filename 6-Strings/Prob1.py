# Problem:
# Take a string from the user and perform the following operations:
#
# 1. Print the string in uppercase
# 2. Print the string in lowercase
# 3. Count total vowels
# 4. Reverse the string
# 5. Check whether the string is palindrome or not
# 6. Replace all spaces with '-'

text = input("Enter a string: ")

# 1,2 - Upper & Lower Case
print('String in Upper Case: ',text.upper())
print('String in Lower Case: ',text.lower())

# 3 - Vowel Counting
count=0
for char in text:
    if char in 'aeiouAEIOU':
        count+=1
print (f"Total Vowel Count in {text} is: {count}")

# 4 - String Reversal
reverse= text[::-1]
print(f"Reversed string is: {reverse}")

# 5 - Palindrome or not
if text==text[::-1]:
    print(f'{text} is Palindrome')
else:
    print(f"{text} is not Palindrome")

# Replace spaces with '-'
new_text= text.replace(' ','-')        
print(f'Replaced String: {new_text}')
