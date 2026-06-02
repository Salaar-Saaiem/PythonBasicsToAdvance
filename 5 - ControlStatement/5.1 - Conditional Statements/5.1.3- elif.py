'''
Write a program to check ticket prices based on age.
   Below 5 → Free
   5 to 17 → Child Ticket
   18 to 59 → Adult Ticket
   60 and above → Senior Citizen Ticket
'''

age = int(input('please enter your Age:'))
if age<=5:
    print('Age Below 5 is free')
elif age>=5 and age<=17:
    print('Child need to pay 599/-')
elif age>=18 and age<=59:
    print('Adults need to pay 999/-')
else:
   print('Senior Citizens are not allowed')