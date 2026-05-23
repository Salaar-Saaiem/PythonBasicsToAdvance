'''
print cubes of numbers from 1 to 10.
'''
total = 0
for i in range(1, 11):
    total = i ** 3            # total = i*i*i
    print(f"Cube of {i} is {total}")