'''
set()  # creates an empty set or converts list in to a set
set is used to store multiple items in a single variable. It is unordered, unchangeable, and does not allow duplicate values. Sets are defined using curly braces {}.
intersection()  # returns the elements that are common in both sets
intersection is used to find the common elements between two sets. It returns a new set containing only the elements that are present in both sets.
'''

list1= [1,2,3,4,3,4,2,6,2,52,6]
list2=[8,5,3,8,92,34,1,34,4]

set1=set(list1)
set2=set(list2)
print(set1, set2)

print(set1.intersection(set2))
#another method
set3 = set1.intersection(set2)
print(set3)
#another method - converting the set to list
print(list(set3))

#lets try on strings
names={'saaiem','Sam','tanishka'}
names2={'saaiem','Arjun','bhavya'}
print(names.intersection(names2))