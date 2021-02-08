'''2. Take two list of numbers of products quantities and prices and calculate total price.
Hint: Use list comprehension and aggregation
Input
product_quantities = [13, 5, 6, 10, 11]
prices = [1.2, 6.5, 1.0, 4.8, 5.0]
Output
Total = 157.1
'''
product_quant=input("Enter product quantities separated by comma : ").split(",")
product_price=input("Enter product price separated by comma : ").split(",")
if len(product_quant)==len(product_price):
    total=sum([float(i)*float(j) for i,j in zip(product_quant,product_price)])
    print("The total price is: ",total)
else:
    print("Please enter complete data")
