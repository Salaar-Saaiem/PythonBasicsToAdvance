'''
to delete an item from a dictionary, 
you can use the del statement or the pop() method. 
Here's how you can do it:

del statement syntax: del dictionary_name[key]
pop() method syntax: dictionary_name.pop(key)
'''

my_dict={
    'Name':'Saaiem', 'Hobbies':['PlayingGuitar', 'Cycling', 'singing'], "Age": 21, 13:'birthdate', "nums": [1,2,3,4,5]
}
print(my_dict)
del my_dict['Hobbies'] # it will give an error because 'Cycling' is not a key in the dictionary, it is a value in the list which is a value of the key 'Hobbies'
print(my_dict)

#to delete the value 'Cycling' from the list which is a value of the key 'Hobbies', we can use the pop() method of the list
my_dict['nums'].pop(1) # it will delete the value at index 1 in the list which is 'Cycling'
print(my_dict)