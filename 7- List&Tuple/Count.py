'''
.count(data) method is used to count the number of occurrences of an element in a list or a tuple.
'''
# Example with a list
my_list = [1, 2, 3, 4, 2, 5, 2,'saaiem', True, True, False, False]
counter=my_list.count(2) #Method 1 - Using a variable to store the count
print(counter)

print(my_list.count(False)) #Method 2 - Directly printing the count without using a variable

tuple_example = 1, 2, 3, 4, 2, 5, 2,'saaiem', True, True, False, False
print(tuple_example.count(2)) #Counting occurrences of 2 in the tuple
