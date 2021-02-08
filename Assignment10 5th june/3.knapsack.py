'''3. Give a list of weight and value pairs for items and a bag with capacity.
Approach:
Calculate the maximum item value that can be carried in the bag.
Note - Items can be carried in parts/fraction.
Input
==========
Items as (value, weight) pairs
Items = [(60, 10), (100, 20), (120, 30))
capacity = 50;
Output
======
240
'''

def knapSack(W, wt, val, n): 
	if n == 0 or W == 0 : 
		return 0
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1)  
	else: 
		return max( val[n-1] + knapSack( W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print("Maximum value in Knapsack =", knapSack(W, wt, val, n))
