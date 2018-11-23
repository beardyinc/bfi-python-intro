number = 15

cond1 = number == 17
cond2 = False
cond3 = True

# if not (not (cond1 or not cond2) and not cond3):
#     print('yes, condition is true')
#     b = 26
#     print(b)

#      False          False
if cond1 or (cond2 or cond3):
    print('yes, its true')
else:
    print('nope')
anotherVariable = "test"
