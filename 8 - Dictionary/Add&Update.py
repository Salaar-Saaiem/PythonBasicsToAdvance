'''adding items to a dictionary
You can add items to a dictionary by assigning a value to a new key. Here's how you can do it:

syntax: dictionary_name[new_key] = new_value
updation syntax: dictionary_name[existing_key] = new_value
'''

my_dict={
    'city': ['kalyan','Mumbai'], 'country':'india'
}
print(my_dict)

my_dict['city']='Thane' # it overwrite my value in the key 'city', i should only add unique key to avoid modification
print(my_dict)

my_dict['District']='saravli'
print(my_dict)