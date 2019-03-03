s = input().split()
n, m = int(s[0]), int(s[1])
s = input().split()
r = 0
for i in range(n):
    val = int(s[i])+r
    print(val // m, end=' ')
    r = val%m
print('')
