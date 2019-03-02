(n, m) = [int(i) for i in input().strip().split(' ')]
count = 0
for i in range(n):
    l = [int(j) for j in input().strip().split(' ')]
    for k in range(0, 2*m, 2):
        if l[k] == 1 or l[k+1] == 1:
            count += 1
print(count)