'''
Dictonaries in Python are created using curly braces {} and consist of key-value pairs. 
Each key is separated from its value by a colon (:), and the pairs are separated by commas. 
Here's how you can create a dictionary:
'''

my_dict={
    'Name':'Saaiem', # key:value, key can be a word and value can be a word as well\
    'Hobbies':['PlayingGuitar', 'Cycling', 'singing'], #one key can have multiple values as well
    "Age": 21, #key or value can be numeric as well
    13:'birthdate',
    "nums": [1,2,3,4,5] #key can be a word and value can be a list as well
}
print(my_dict)

'''
key should be unique in a dictionary, if you try to assign a value to an existing key, it will overwrite the previous value.
'''