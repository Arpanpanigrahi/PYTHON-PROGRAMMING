import os

file_obj=open(r"D:\\Python programs\sowpods.txt")
word_list=file_obj.readlines()
clc_list=[word.strip() for word in word_list()]
file_obj.close()
