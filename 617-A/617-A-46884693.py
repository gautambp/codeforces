n = int(input())
min_step = 0
for s in [5, 4, 3, 2, 1]:
    min_step += int(n/s)
    n = (n%s)
print(min_step)