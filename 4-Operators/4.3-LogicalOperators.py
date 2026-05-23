'''
Logical operators are used to compare multiple values at once
    it also return the output in boolean such as true/false,  yes/no

and - All COnditions should be true to return true, otherwise false
or - Atleast one condition shoukd be true to return true other wise false
not - it operates on single value, and it reverses the output, like if output is true, itll reverse it as false
'''

a=10
b=20

print(a>5 and b>15)   #and operator eg for all true condition
print(a>5 and b<10)   #and operator eg for one true one false
print(a>5 or b<10)    #or operator eg for one false one true
print(a>30 or b> 40)  #or operator for all false value
print(not(a==10))     #a is true but itll reverse it and output false

print('\n','\n')

# Example 2 using SET 
sam={
    'physics':89,
    'maths':91,
    'hindi':30
}
result=(sam['physics']>34 and sam['maths']>34 and sam['hindi']>34)

if result == True:
    print('Pass')
else:
    print('Fail')