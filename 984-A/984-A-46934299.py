n = int(input())
a = [int(i) for i in input().strip().split(' ')]
sa = sorted(a)
if n%2 == 0:
    print(sa[int(n/2)-1])
else:
    print(sa[int(n/2)])
