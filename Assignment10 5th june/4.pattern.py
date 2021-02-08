'''4. Consider a sorted sequence of number with following pattern 2^i × 3^j × 5^k
Approach: Take input N from the user and output the Nth number in the sequence
'''

n=int(input("Enter the Range"))
k=int(input("Enter the position"))
random=1
ls=[]
ls.append(random)
while(random<n):
    random+=1
    if(random%2==0 or random%3==0 or random%5==0)and random%7!=0:
        ls.append(random)
print(ls)
print(ls[k-1])

