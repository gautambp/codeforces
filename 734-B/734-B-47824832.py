def getMin(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    if n2 <= n1 and n2 <= n3:
        return n2
    return n3
    
(k2, k3, k5, k6) = list(map(int, input().split()))

total = 0
m = getMin(k2, k5, k6)
total += 256*m
k2 -= m
k5 -= m
k6 -= m
m = getMin(k2, k3, k3)
total += 32*m
k2 -= m
k3 -= m

print(total)