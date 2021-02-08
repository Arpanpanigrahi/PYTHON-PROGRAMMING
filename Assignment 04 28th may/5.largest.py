''' 5. GIVEN  A LIST 'A' AND NUMBER N , FIND THE NTH LARGEST NUMBER.
       EXAMPLE: IF THE INPUT LIST IS[5,2,1,7,4] AND N IS 3.
       THE 3RD LARGEST NUMBER IS 4. '''

a=[]
a=list(map(int,input().split()))
a.sort()
m=len(a)
n=int(input())
print(a[m-n])



'''IN MY CASE SUPPOSE USER INPUTS 1 2 3 4 5
    THEN FIRST LARGEST=5
         SECOND LARGEST=4
         THIRD LARGEST=3
         AND SO ON.... '''
