n = int(input())
lst = list(map(int,input().split()))
a = list(set(lst))
b = [i for i in a if lst.count(i) == 2]
print(*b)
