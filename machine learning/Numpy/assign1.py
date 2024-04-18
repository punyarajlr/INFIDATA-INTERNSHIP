import numpy as np

a1 = np.arange(10, 101, 10)
print(a1)

numbers = range(10, 101, 10)
a2= np.array(list(numbers))
print(a2)

a3=np.array([])
print(a3)

a4=np.random.randint(1,6,size=10)
print(a4)

a5=np.random.randint(1,11,size=3*4)
ran=a5.reshape(3,4)
print(ran)

a6=np.array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]])
s1=a6[0,:5]
print(s1)

s2=a6[3,:5]
print(s2)

print(a6[2,3])

s3=a6[:,0]
print(s3)

print(a6[:, 3:])

s4=a6[1,:5]
print(s4)