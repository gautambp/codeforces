n = int(input())
if n >= 0:
    print(n)
elif n >= -10:
    print(0)
else:
    n1 = int(str(n)[:-1])
    n2 = int(str(n)[:-2]+str(n)[-1])
    print(n1 if n1 > n2 else n2)