'''
.reverse() method is used to reverse the order of the elements in a list. 
It modifies the original list in place and does not return a new list.
.reverse() method does not work with tuples because tuples are immutable (cannot be changed after they are created).
'''

nums = [1,2,3,4,5,6]
nums.reverse()
print(nums)

char=['Saaiem', 'Tanishka', 'Siddesh', 'Arjun']
char.reverse()
print(char)

print(nums.reverse()) #it will return None because reverse() method modifies the original list and returns None