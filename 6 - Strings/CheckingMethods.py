'''
these are the operations to check string
.startswith('character') -> used to check whether the string starts with the character or not, it return in boolean and it is diff from membership where we used to check whether the word is innit or not
.endswith('character')
.isAlpha -> to check if all characters in string is alphabets or not
.isDigit -> to check whether all characters in string are digits or not
'''

str='SaaiemSalaar'
print(str.startswith('s'))
print(str.startswith('S'))
print(str.endswith('r'))
print(str.isalpha())
print(str.isdigit())
print(str.isnumeric())
