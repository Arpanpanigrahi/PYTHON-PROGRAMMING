'''3. Take a sentence and output a dictionary with word as the key and number of characters in the word as value
Hint: Use dictionary comprehension
'''

S="My Name is Arpan Panigrahi"
x=S.split(" ")
print(x)
new_dict={}
for i in range(len(x)):
    new_dict[x[i]]=len(x[i])
print(new_dict)
    
