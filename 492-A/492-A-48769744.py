n = int(input())
l = 1
s = 0
while True:
    lc = (l * (l+1)) // 2
    if (s+lc) > n:
        print(l-1)
        break
    l += 1
    s += lc