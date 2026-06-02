profile={
    'name':'Saaiem',
    'age':22,
    'ChosenSubjects': ['MachineLearning','Blockchain','ArtificialIntelligence','EdgeComputing']
}
for i in profile:
    print(i)

# print only keys
print('\nKeys in the dictionary:')
for i in profile.keys():
    print(i)

# Print only Values
print('\nValues in the dictionary:')
for i in profile.values():
    print(i)

# Print keys and values both
print('\nPairs in the dictionary:')
for i in profile.items():
    print(i)