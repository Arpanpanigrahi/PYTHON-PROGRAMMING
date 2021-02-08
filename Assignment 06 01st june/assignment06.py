#ASSIGNMENT DAY 6
'''
#Q1)Create an add function that is agnostic to number of inputs Example: My_Custom_Add(1,2,3,4,5) Output: 15

res=0
def My_Custom_Add():
    a=list()
    sum=0
    a=input(("Enter the elements that are to be added (separated by space) that are to be added: ")).split()
    for ele in a:
        sum=sum+int(ele)
    return sum

res=My_Custom_Add()
print("This sum of the entered elements is: ",res)


#Alternate
def My_Custom_Add(*args):
    sum=0
    for i in args:
        sum=sum+int(i)
    return sum
res=My_Custom_Add(1,2,3,4,5,6)
print("The  Result is : ",res)
'''

'''
#Q2)Accept two sequence of number, one for distance another for time and return a list of speeds
Example: Input Format:
• 10 20 30 40 50
• 1 5 3 2 4
Output format [10.0, 4.0, 10.0, 20.0, 12.5]

def input_data():
    li=input().split()
    return li
def calc_speed(li1,li2):
    speed=list()
    if len(li1)==len(li2):
        for d,t in zip(li1,li2):
            if t!=0:
                spd=int(d)/int(t)
                speed.append(spd)
            else:
                print("Time can't bec zero")
                break
            return speed
        else:
            print("Please enter valid values")
print("Enter the distance separted by space : ")
li1=input_data()
print("Enter the time separated by space : ")
li2=input_data()
speed=calc_speed(li1,li2)
print("The speed sequence is: ",speed)
'''

'''
# Q3)Given a list of products, print out the name of all the products with a price higher than 10 Hint: Use Dictionary products = [
{'name': 'orange', 'price': 20},
{'name': 'apple', 'price': 8},
{'name': 'banana', 'price': 10},
{'name': 'kiwi', 'price': 30}
]
'''

products = [{'name': 'orange', 'price': 20},{'name': 'apple', 'price': 8},{'name': 'banana', 'price': 10},{'name': 'kiwi', 'price': 30}]
for i in products:
    if i['price'] > 10:
        print(i['name'])

