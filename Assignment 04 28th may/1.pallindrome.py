''' 1.CHECK FOR PALLINDROME IN A STRING WITHOUT USING LOOP STATEMENT.'''
a=[]
a=input()
''' reverses the list '''
if (a==a[::-1]): 
    print("the list is a pallindrome")
else:
    print("the list is not pallindrome")
