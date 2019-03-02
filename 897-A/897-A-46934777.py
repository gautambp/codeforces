(n,m) = [int(i) for i in input().strip().split(' ')]
s = list(input().strip())
for _ in range(m):
    (l,r,c1,c2) = [i for i in input().strip().split(' ')]
    for i in range(int(l)-1, int(r)):
        if s[i] == c1:
            s[i] = c2
print(''.join(s))