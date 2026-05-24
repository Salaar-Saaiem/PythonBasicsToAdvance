'''
.pop() is used is list to remove the element from specified index
in .remove() we pass data directly, but in pop() we provide index no.
.pop() method is used to remove an element from a list at a specified index and returns the removed element.
It modifies the original list. If the specified index is out of range, it raises an IndexError.
The .pop() method does not work with tuples because tuples are immutable (cannot be changed after they are created).
'''

str=['Saaiem', 'Salaar', 'Sam']
str.pop(1)
print(str)

'''
we can do this to see the popped item, ITS IMP AND WILL BE USED IN DSA
'''
popped=str.pop(1)
print(popped)