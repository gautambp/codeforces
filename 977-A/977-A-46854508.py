(ns, ks) = input().split(' ')
n = int(ns)
k = int(ks)

while k > 0:
    if n % 10 == 0:
        n = int(n/10)
    else:
        n -= 1
    k -= 1
print(n)