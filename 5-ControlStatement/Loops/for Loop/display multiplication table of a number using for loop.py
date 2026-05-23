'''
display multiplication table of a number using for loop
'''
num=int(input('Enter the number u would like a multiplication table of: '))
total = 0
for i in range (1,11):
    total = i * num
    print(f'{num} x {i} = {total}')
    i+=1