'''4. Run the code below to generate a matrix
Approach:
take an input character as target
print the row index and column index if the character is found
Else print "Not found"
Input
Enter Target character : h
Output
2 4
table = [list("abcd"),list("efgh"),list("ijkl")]
'''

a=list("abcd")
b=list("efgh")
c=list("ijkl")
table = [a,b,c]
flag=0
ele=input("Enter the character : ")
for row_index,row in enumerate(table):
    for column_index,column in enumerate(row):
        if column==ele:
            flag==1
            print(row_index+1,column_index+1)
            break
if flag==0:
    print("Element Not Found")


