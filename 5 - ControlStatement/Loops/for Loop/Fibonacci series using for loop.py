'''
Fibonacci series using for loop.
it is a series, where the value of current is sum of last 2 digit
eg: 1,2,3,5,8,13.....
'''
a=0
b=1
for i in range(1,11):
    c = a+b
    a=b
    b=c
    print(c, end=" ")
