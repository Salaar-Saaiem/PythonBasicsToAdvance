'''
to update the list at specific index number

'''

str = [1,2,3,4,5,6,7,8,9]
print (str[2])

print(f"before updation: {str}")
str[2]='Saaiem' 
print(f"After Updation: {str}")

'''
if multiple elements need to be updated, use slicing
'''

str1=[1,2,3,4,5,6]
str1[0:3]= 10,20,30
print(str1)