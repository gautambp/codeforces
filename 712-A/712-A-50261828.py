n = int(input())
a = input().split()
for i in range(n-1):
    print(int(a[i])+int(a[i+1]), end=' ')
print(a[n-1])