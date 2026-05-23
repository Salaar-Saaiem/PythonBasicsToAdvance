'''
PROBLEM STATEMENT: Take two numbers form the users and do the calculation that user desire (+,-,*,/)
'''

num1=int(input('Enter First Number:'))
num2=int(input('Enter Second Number'))
choice=input('What would u like to do +,-,*,/: ')

if choice == '+' or choice == 'addition' or choice == 'Addition' or choice == 'add' or choice == 'Add':
    print(f"Addition of two values are:", num1+num2)

elif choice in ['-', 'Substract', 'minus', 'Minus', 'substract']:
    print(f"Substracted Value of two number is {num1-num2}")
    
elif choice in ['mult', 'multiplication', '*', 'Mult', "Multiplication"]:
    print (f"Multiplication value of two elements are:{num1*num2}")