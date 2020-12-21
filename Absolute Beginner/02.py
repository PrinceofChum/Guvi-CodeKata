N=int(input())
result=1
if N==1:
    print (1)
elif N>1:
    while(N>1):
        result*=N
        N-=1
        
print (result)
