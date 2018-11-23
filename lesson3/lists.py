mylist = ['apple', 'banana', 'orange', 'raspberry']
mylist.append('lemon')

print(mylist)
# mylist.remove('banana')

mylist.pop()
# equivalent to:
del mylist[3]
print(mylist)

number = 17
print(number)
del number

# complicated, not easy to read
for elem in mylist:
    if elem == 'orange':
        print('yes we have an orange!')

# 'pythonic'
if 'orange' in mylist:
    print('orange found, but shorter!')
