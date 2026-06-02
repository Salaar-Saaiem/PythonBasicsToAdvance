'''
length operation is used in string to identify the length (characters present in the string)
Function: len()
it calculates the spaces as well
'''

name='Saaiem Salaar'
print(len(name))

name1='SaaiemSalaar'
print(len(name1))

name2='Saaiem@12Salaar'
print(len(name2))

#to caluculate the words in the sentance we can use split function and then count the length of the list
sentance = 'Hello World'
words = sentance.split()    
print(len(words))