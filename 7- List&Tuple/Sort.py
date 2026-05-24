'''.sort() method is used to sort the list in ascending order by default. It modifies the original list.
.sort() method does not work with tuples because tuples are immutable (cannot be changed after they are created).
'''

nums = [5, 2, 9, 1, 5, 6]
nums.sort()
print('Sorted list of numbers: ', nums)


''''''''''''''''''''''''''''''''''''''''''''''''''''''


names=['saaiem','apple','mango','lucifer']   #it can sort words as well in alphabetically manner
names.sort()
print('Sorted list of characters: ',names)


''''''''''''''''''''''''''''''''''''''''''''''''''''''

num=[1,3,6,2,6,4,3]
print(num.sort())       # dont return anything because sort() method modifies the original list and returns None
print(num)             # the original list is modified and sorted in ascending order    