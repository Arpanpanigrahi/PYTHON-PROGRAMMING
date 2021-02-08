#1. Join two sorted lists such that the final list is also sorted

x_list1=[1, 5, 6, 9, 11]
y_list2=[3, 4, 7, 8, 10]
print(" The list 1 is : " +str(x_list1))
print(" The list 2 is : " +str(y_list2))
z=sorted(x_list1+y_list2)
print("Final sorted list : " + str(z))
