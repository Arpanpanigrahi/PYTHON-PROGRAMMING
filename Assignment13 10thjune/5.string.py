#5. Take a string as input and do the following without using any string functions:
#i. Remove if there are any duplicates
#ii. Remove if there are any special characters
#iii. Change the case of each character


#5. Take a string as input and do the following without using any string functions:
#i. Remove if there are any duplicates
#ii. Remove if there are any special characters
#iii. Change the case of each character


def remove_dupli(string1):
    li=[]
    for i in string1:
        if i not in li:
            li.append(i)
    string1="".join(li)
    print("The string after removing duplicates is        :",string1)

def special_char(string1):
    num=['0','1','2','3','4','5','6','7','8','9']
    string2=[]
    for i in string1:
        if 'A'<=i<='Z' or 'a'<=i<='z' or i in num:
            string2.append(i)
    string1="".join(string2)
    print("The string after removing special characters is:",string1)

def change_case(string1):
    li2=[]
    for i in string1:
        if 'a'<=i<='z':
            i=chr(ord(i)-32)
            li2.append(i)
        elif 'A'<=i<='Z':
                i=chr(ord(i)+32)
                li2.append(i)
        else:
            li2.append(i)
    string1="".join(li2)
    print("The string after changing the case is           :",string1)

string1=input("Enter the string: ")
string1=list(string1)
remove_dupli(string1)
special_char(string1)
change_case(string1)
