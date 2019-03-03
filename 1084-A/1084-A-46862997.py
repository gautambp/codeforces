n = 3
n = int(input())
astr = '0 2 1'.strip().split(' ')
astr = input().strip().split(' ')
min_cnt = None
for x in range(n):
    total = 0
    for y in range(len(astr)):
        p = int(astr[y])
        if x == y:
            total += p*(4 * x)
        else:
            total += p*(abs(x-y) + y + x + x + y + abs(x-y))
    if min_cnt == None or total < min_cnt:
        min_cnt = total
print(min_cnt)
