"""
Set variable only return the unique values in the list, 
suppose there is list [1,2,2,3,4,4,5,5]
    we only need unique values from this list and in arranged manner, so we will use set here by using {} this 
"""

unique_numbers = {1,2,3,4,3,4,2,6,7,8,5}
print(unique_numbers)


'''
Frozen set- this is another type of set where u can not modify the set, u can only see it
    in set u can modify it as well
'''

unique_num = frozenset([1,2,3,2,4,3,5,7,6])
print(unique_num)