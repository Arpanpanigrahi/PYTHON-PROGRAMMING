# 5) Write a program to find Leap year

#User enters the yr.
year=int(input("Enter year:"))

#Condition for leap yr.
if(year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year:")
elif(year % 100 == 0):
    print(year, "is not a leap year:")
elif(year % 400 == 0):
    print(year, "is a leap year:")
else:
    print(year, "is not a leap year:")
