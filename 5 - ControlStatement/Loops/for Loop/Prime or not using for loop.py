'''
prime or not using for loop.
'''

num=int(input('Enter the number u wish to know whether it is Prime or not: '))
prime=True

if num <=1:
    prime = False
else:
    for i in range(2,num):
        if num%i==0:
            prime=False
            break

if prime:
    print(f"The Number {num} is a Prime Number")
else:
    print(f"The Number {num} is not a Prime Number")