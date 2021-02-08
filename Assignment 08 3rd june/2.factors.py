'''
2. Find the total factors for a given integer N.
Ex: 24 has 1, 2, 3, 4, 6, 8, 12, 24 total 8 factors. So, if the input is 24 output
should be 8
'''


num=int(input("enter a number"))
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)
print ("Factors of {} = {}".format(num,factors))



'''
#Alternate Method

def factors(x):
   print("The factors of x are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 24
factors(num)
'''
