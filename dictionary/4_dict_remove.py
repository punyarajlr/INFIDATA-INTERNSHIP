#remove a particular item in a dictionary by using the poop() method
#this method removes one item with the provided key and returns the value
#popitem() method can be used to remove and return on arbitary(key ,value)
#item pair from the dictionary
#all the items can be removed at once,using the clear() method
#we can also use the del keyword to remove individual items or the entire
#dictionary itself.
d1={1:1,2:4,3:9,4:16,5:25,6:36}
print(d1)

print("pop value id:",d1.pop(2))
print("updated dictionary is:",d1)

print("pop item is:",d1.popitem())          #remove an arbitary item,return(key,value)
print("updated dictionary is:",d1)

d1.clear()   #remove all  items
print("updated dictionary is: ",d1)

del d1                    #delete the dictionary
print(d1)