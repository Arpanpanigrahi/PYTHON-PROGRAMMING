import os
import string
file=open(r"C:\Users\hp\Desktop\Python programs\Assignment11 8th june\sowpods.txt")
wordlist=[word.strip() for word in file.readlines()]
file.close()


#2)

for word in wordlist:
    if 'UU' in word:
        print(word)


'''
#4)
vowels='AEIOU'
for word in wordlist:
    li=[]
    for letter in word:
        if letter in vowels:
            li.append(letter)
    li=set(li)
    if len(vowels)==len(li):
        print(word,end=' ')
                
'''

'''
#5)

for word in wordlist:
    if word==word[::-1]:
        print(word)
'''
'''
#3
for letter in string.ascii_uppercase:
    flag=True
    for word in wordlist:
        if letter*2 in word:
            flag=False
            break
    if flag:
        print(letter)

'''
        
