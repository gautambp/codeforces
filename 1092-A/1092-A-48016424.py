import string

for _ in range(int(input())):
    s = input().split()
    n = int(s[0])
    k = int(s[1])
    base = string.ascii_lowercase[:k]
    print(base*(n//k) + base[:(n%k)])
