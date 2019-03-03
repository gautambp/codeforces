p_nos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def findDivisible(l, r):
    for i in range(l, r+1):
        for p in p_nos:
            if i*p <= r:
                return (i, i*p)
    return (-1, -1)

for _ in range(int(input())):
    s = input().split()
    l = int(s[0])
    r = int(s[1])
    (n1, n2) = findDivisible(l, r)
    print('{} {}'.format(n1, n2))
