# Problem:
# Take a sentence from the user and perform the following operations:
#
# 1. Count total uppercase letters
# 2. Count total lowercase letters
# 3. Count total digits
# 4. Count total special characters
# 5. Remove all spaces from the string
# 6. Find whether the sentence contains only alphabets or not

text=input('Please Enter the Sentance: ')

# 1. Count total uppercase letters
upcount=0
for char in text:
    if char.isupper():
        upcount+=1
print(f"Total no. of Uppercases are {upcount}")


# 2. Count total lowercase letters
lowcount=0
for char in text:
    if char.islower():
        lowcount+=1
print(f"Total no. of Lowercases are {lowcount}")


# 3. Count total digits
digit=0
for char in text:
    if char.isdigit():
        digit+=1
print(f"Total no. of Digits are {digit}")


# 4. Count total special characters
spchar=0
for char in text:
    if not char.isalnum() and char == ' ':
        spchar+=1
print(f"Total no. of Special Characters are {spchar}")


# 5. Remove all spaces from the string
print(text.replace(' ', ''))


# 6. Find whether the sentence contains only alphabets or not
replaced=text.replace(' ','')
alp=replaced.isalpha()
if alp is True:
    print('Sentance only have alphabets')
else:
    print('Sentance does not only have alphabets')