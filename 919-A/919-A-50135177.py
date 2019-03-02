s = input().split()
n, m = int(s[0]), int(s[1])
min_p = None
for i in range(n):
    s = input().split()
    a, b = int(s[0]), int(s[1])
    if min_p == None or min_p > a/b:
        min_p = a/b
print(min_p*m)