n = int(input("enter an number"))
sum=0

while(n > 0):
    dig = n % 10
    sum = sum + dig
    n = n // 10
print("\n sum of the digits:" ,sum)
