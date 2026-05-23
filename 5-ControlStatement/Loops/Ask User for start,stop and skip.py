'''FOR SINGLE DIGIT SKIP'''
start=int(input('Enter the Number from which Counting should Start: '))
stop=int(input("Enter the Number where the list should Stop: "))
skip=int(input("Enter the Number u want to SKIP from this List: "))

for i in range(start, stop+1):
    if i==skip:
        continue
    print(i)


'''FOR MULTIPLE SKIP'''
start=int(input('Enter the Number from which Counting should Start: '))
stop=int(input("Enter the Number where the list should Stop: "))
skip=list(map(int, input("Enter the Number u want to SKIP from this List: ").split()))

for i in range(start, stop+1):
    if i in skip:
        continue
    print(i)

