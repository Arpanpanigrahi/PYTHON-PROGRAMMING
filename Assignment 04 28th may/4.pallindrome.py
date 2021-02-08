'''4.Write a program to find palindromic numbers between 2 numbers
     Hint: Palindromic number between 10 to 50 are 11, 22, 33, 44 [Marks: 3]'''

minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))

print("Palindrome Numbers between %d and %d are : " %(minimum, maximum))
for num in range(minimum, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')


 
