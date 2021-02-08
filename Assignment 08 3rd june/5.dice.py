# 5. Assume a fair dice roll using a similar random integer generation code above roll for 500 times and print the number of times 1 to 6 has appeared.

import random
c1=c2=c3=c4=c5=c6=0
for i in range(500):
    rolldice=random.randint(1,6)
    if rolldice==1:
        c1+=1
    elif rolldice==2:
        c2+=1
    elif rolldice==3:
        c3+=1
    elif rolldice==4:
        c4+=1
    elif rolldice==5:
        c5+=1
    elif rolldice==6:
        c6+=1
print(c1,c2,c3,c4,c5,c6)
