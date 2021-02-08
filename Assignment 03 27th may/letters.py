# 3) Write a program that accepts a sentence and calculate the number of letters and digits.
#Example: Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

letters=0
digits=0
for c in a:
    if c.isdigit():
        digits = digits + 1
    else:
        letters=letters + 1

print("Letters s" ,letters)
print("Digits" ,digits)
