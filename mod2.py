	
import random
 
mylist = []
 
for i in range(4):
    i = random.randint(1,100)
    mylist.append(i)
 
mylist.sort()
 
for i in range( len(mylist)):
    print(mylist[i])

