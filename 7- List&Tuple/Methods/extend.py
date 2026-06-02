'''
Suppose there are two list, and u want to extent list 1 with the elements of list 2
it is diff from concatination bcoz concatination creates a new list to combine both, even if u use it in print function-it creates temporary list
syntax: list1.extend(list2)

'''

str1=['Shaikh', 'Saaiem']
str2=['Salaar']

str1.extend(str2)
print(str1)
