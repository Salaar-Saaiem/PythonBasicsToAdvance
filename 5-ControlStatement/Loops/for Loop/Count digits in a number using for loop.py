'''
count digits in a number using for loop.
'''

count = 0
number=list(input('Enter the Number of which u wish to count digits: ')) # cant use int or float bcoz it is not iterable
for i in number: 
    count += 1
print(count)