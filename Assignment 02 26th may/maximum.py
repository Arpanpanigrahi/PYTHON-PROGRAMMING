list1 = []
maxno = 0
n=int(input("How many elements are there in the list? : "))
print("Enter the elements of the list: ")
for i in range(n):
    element = int(input())
    list1.append(element)
for i in list1:
    if(i > maxno):
        maxno = i
print("The maximum element in the list is : ",maxno)
