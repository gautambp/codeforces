s = input().split()
n = int(s[0])
m = int(s[1])
a = n*(n+1)//2
b = m%a
for i in range(1, n+1):
    if b >= i:
        b -= i
    else:
        break
print(b)