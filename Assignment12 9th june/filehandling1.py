#2)a. Print the longest pallindrome in sowpods.txt
'''
import os
import string
file=open("sowpods.txt")
word_list=[word.strip() for word in file]
file.close()

li=[]
for word in word_list:
    if word==word[::-1]:
        li.append(word)
res=max(li,key=len)
print(res)
'''


#2)b. Print the words that are in sonnet_words.txt but not in sowpods.txt

file_obj_sow = open(r"sowpods.txt")
file_obj_son = open(r"sonnet_words.txt")
sow_list = [word.strip() for word in file_obj_sow.readlines()]
son_list = [word.strip() for word in file_obj_son.readlines()]
file_obj_sow.close()
file_obj_son.close()

import time
tic = time.time()
for son in son_list:
    if son not in sow_list:
        print(son)
print(time.time()-tic)
