s = input().split()
n = int(s[0])
t = int(s[1])
l = list(input())
while t > 0:
    i = 0
    while i < n:
        if i < n-1 and l[i] == 'B' and l[i+1] == 'G':
            l[i] = 'G'
            l[i+1] = 'B'
            i += 1
        i += 1
    t -= 1
print(''.join(l))
