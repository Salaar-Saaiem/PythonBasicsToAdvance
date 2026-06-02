'''
If a code has multiple operators in one variable such as 
    result= a + b * d / e
compiler execute it in PEMDAS 
    perenthese () - 1st priority
    exponent ** - 2nd priority
    multiplication and division * or / - 3rd and 4th priority
    addision and substraction + or - - 5th and 6th priority

example --> (2 + 3) ** 2 * 4 / 2 - 5 + 1

How PEMDAS works here:

Parentheses → (2 + 3) = 5
Exponent → 5 ** 2 = 25
Multiplication → 25 * 4 = 100
Division → 100 / 2 = 50
Subtraction → 50 - 5 = 45
Addition → 45 + 1 = 46
'''

sol = (2 + 3) ** 2 * 4 / 2 - 5 + 1
print(sol)