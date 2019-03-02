(d1, d2, d3) = list(map(int, input().split()))
if d1+d2 < d3:
    print(2*(d1+d2))
else:
    if d1 > d3 and d2 > d3:
        if d1 < d2:
            print(2*(d1+d3))
        else:
            print(2*(d2+d3))
    elif d1 > d3:
        if d1 > d2+d3:
            print(2*(d2+d3))
        else:
            print(d1+d2+d3)
    elif d2 > d3:
        if d2 > d1+d3:
            print(2*(d1+d3))
        else:
            print(d1+d2+d3)
    else:
        print(d1+d2+d3)