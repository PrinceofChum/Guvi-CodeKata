n=int(input())
l=list(map(int, input().split()))
print ('1') if sum(l)%2==0 and sum(l)%3==0 and sum(l)%5==0 else print ('0')
