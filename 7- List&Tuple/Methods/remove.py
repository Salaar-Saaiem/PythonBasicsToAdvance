'''
.remove() deletes the element at specified data, we dont give index position here-directly the data!
.remove() method is used to remove the first occurrence of a specified value from a list. 
It modifies the original list. If the specified value is not found in the list, it raises a ValueError. 
The .remove() method does not work with tuples because tuples are immutable (cannot be changed after they are created).
'''

name=['Saaiem','Salaar','Shaikh']
name.remove('Shaikh')
print(name)