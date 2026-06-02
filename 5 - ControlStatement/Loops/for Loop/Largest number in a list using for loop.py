"""
15. Write a program to find largest number in a list using for loop.
"""
largest=0
#elements= 2,3,5,1,74,23,52,62
elements=list(map(int, input('Enter the numbers using spaces : ').split()))
for i in elements:
    if largest<=i:
        largest = i
print(largest)