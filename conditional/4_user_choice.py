n1=int(input("enter the num1"))
n2=int(input('enter the num2'))
ch=int(input("enter ur choice 1:ADD 2:SUB 3:MUL 4:DIV 5:MOD"))
if(ch==1):
    res=n1+n2
    print("add of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==2):
    res=n1-n2
    print("sub of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==3):
    res=n1*n2
    print("mul of {0} and {1} is {2}".format(n1,n2,res))
elif(ch==4):
    res = n1/n2
    print("div of {0} and {1} is {2}".format(n1, n2, res))
elif(ch==5):
    res = n1%n2
    print("mod of {0} and {1} is {2}".format(n1, n2, res))
else:
    print("invalid choice")