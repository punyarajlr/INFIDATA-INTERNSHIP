l1=[]
for i in range(6):
     l2=int(input("enter the numbers"))
     l1.append(l2)
print("elements \t\t frequency")
for i in l1:
    print(i,end="\t")
    print(l1.count(i))
