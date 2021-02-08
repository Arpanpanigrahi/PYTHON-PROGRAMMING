n=int(input("enter no:"))
temp=n
reverse=0
while(n>0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if(temp==reverse):
    print("Pallindrome")
else:
    print("not palllindrome")
