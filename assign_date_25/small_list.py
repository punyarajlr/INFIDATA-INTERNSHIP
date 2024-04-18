l1 = []
s = int(input('How many elements you want to enter '))

print('Enter',str(s),'positive numbers')

for i in range(s):
    data = int(input())
    l1.append(data)

min = 0
for data in l1:
    if data < min:
        min = data

print('The smallest number in list is', min)