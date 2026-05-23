num=int(input('Enter the number u want the multiplication table of '))
total=0
i =1
while i<=10:
    total = i * num
    print(f"{num} x {i} = {total}")
    i += 1