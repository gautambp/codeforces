s = input().split()
n = int(s[0])
m = int(s[1])
r = None
c = None
for i in range(n):
    s = input()
    idx = s.find('B')
    if idx >= 0 and r == None:
        cnt = s.count('B')
        r = i+1+cnt//2
        c = idx+1+cnt//2
print('{} {}'.format(r, c))
