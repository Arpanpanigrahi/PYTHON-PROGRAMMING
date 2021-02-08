
# 3. Write a program that accepts a sentence and calculate the number of letters
#     and digits. Example: Suppose the following input is supplied to the
#     program: hello world! 123! Then, the output should be: LETTERS 10 DIGITS 3


s = 'hello world! 123!'
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])
