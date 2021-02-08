'''1. Take two list of numbers and generate a list of tuples that are combo of the numbers such that two numbers in the pair are not equal.
Hint: Use list comprehension
Input
x = [1,2,3]
y = [1,2,3]
Output
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
'''

x = [1,2,3]
y = [1,2,3]
output=[(a,b) for a in x for b in y if a!=b]
print(output)
