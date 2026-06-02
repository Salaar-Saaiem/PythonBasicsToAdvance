'''
factorial of a number using for loop.
'''

factorial=1
num=int(input('Enter the number u would like to calculate the factorial of: '))
for i in range(1,num+1):
    factorial= num * i
    #print(factorial)   #uncomment to see simulation
print(f"Factorial of Number {num} is {factorial}")