'''
break statement is used in loops to stop loop at certain iteration
'''

'''Breaking looop when 6 is found'''
for i in range(1,11):
    if i==6:
        break
    print (i)

'''Breaking loop when saaiem is found'''
name = 'sam', 'salaar', 'saaiem', 'lucifer'
for char in name:
    if char == 'saaiem':
        print(char)
        break
    