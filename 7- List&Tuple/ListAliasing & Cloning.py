'''
Suppose we have a list and 2nd list is pointing at list 1, 
changes in list one will reflect changes in list 2 as well
'''
list1=[1,2,3,4,5]
list2=list1
print(f"list 2 before updation of list 1 {list2}")
list1[0:3] = 10,20,30
print(f"list 2 After updation of list 1 {list2}")

'''
now if we dont want to reflect the changes result in list 2, like we dont want to make changes and keep both seperate
we use .copy() function
'''
names1=["Saaiem",'sam','salaar']
names2=names1.copy()
print(f"lists before cloning {names1} {names2}")
names2[0:2]= ['Saiem', 'Tanishka']
print(f"lists after cloning {names1} {names2}")