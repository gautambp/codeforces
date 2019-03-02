a = int(input())
b = int(input())
d = abs(a-b)
if d == 1:
    print(1)
else:
    if d%2 == 1:
        n = d // 2
        s1 = (n*(n+1)) // 2
        s2 = ((n+1)*(n+2)) // 2
        print(s1+s2)
    else:
        n = d // 2
        s1 = (n*(n+1)) // 2
        print(s1+s1)