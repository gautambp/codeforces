n = int(input())
l = list(map(int,input().split())) 
l_max = max(l)
print(l_max-25 if l_max > 25 else 0)