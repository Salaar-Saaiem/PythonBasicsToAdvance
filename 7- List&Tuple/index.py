'''
.index('data') is used to know the index number of given data in the list
u have to creat a variable for it, as u can see below, ive created indexed variable to save the index number
'''

name=['saaiem','salaar','sam']
indexed=name.index('salaar') #create variable to store the index number
print(indexed) 

print(name.index('saaiem')) #Method 2- use it in print function directly, no need to create variable

str_tuple=1,2,3,4,5,6,7,8,9,10
print(str_tuple.index(5)) #index method also works for tuple, it will give the index number of 5 in the tuple   