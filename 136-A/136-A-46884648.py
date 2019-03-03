n = int(input())
l = [None]*n
s = input().strip().split(' ')
for i in range(n):
    l[int(s[i])-1] = i+1
for i in l: print(i, end=' ')
print('')
