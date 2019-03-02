n = int(input())
l = list(map(int, input().split()))
c = 0
bi = 0
ba = 0
for i in range(n):
    if i%3 == 0:
        c += l[i]
    elif i%3 == 1:
        bi += l[i]
    elif i%3 == 2:
        ba += l[i]
print(('chest' if c > bi and c > ba else 'biceps' if bi > c and bi > ba else 'back'))