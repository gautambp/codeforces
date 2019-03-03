n = int(input())
s = input()
l = list(s[::-1])
i = 1
d = ''
while len(l) > 0:
    d += l[len(l)-1]
    for _ in range(i):
        l.pop()
    i += 1
print(d)
