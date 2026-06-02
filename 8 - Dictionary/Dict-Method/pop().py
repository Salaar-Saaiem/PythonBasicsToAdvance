emp_profile={
    'name':'Saaiem',
    'age':21,
    'salary':40000
}
'''
dict.pop() method is used to delete a key from the dictionary
'''
popped=emp_profile.pop('age')
print(popped)
print(emp_profile.items())