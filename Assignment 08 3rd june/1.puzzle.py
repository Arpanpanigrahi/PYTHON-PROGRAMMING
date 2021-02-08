'''1. Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and
94 legs among the chickens and rabbits in a farm. How many rabbits and how many
chickens do we have?
Hint: Use for loop to iterate all possible solutions.
'''

def solve(numheads,numlegs):

    ns='No solutions'
    for i in range(numheads+1):
        j=numheads-i
        if (2*i)+(4*j)==numlegs:
            return i,j
    return ns,ns


numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)



'''
#Alternate Method
def solve(heads,legs):
    errormessage="No solution"
    chickencount=0
    rabbitcount=0
    ans=False  
    for i in range(heads+1):
        j=heads-i
        if (2*i)+(4*j)==legs:
            chickencount=i
            rabbitcount=j
            ans=True
            break
    if (ans==True):
        print(chickencount,rabbitcount)
    else:
        print(errormessage)
solve(35,94)
'''
