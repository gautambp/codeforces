n = int(input())
l = list(map(int, input().split()))
max_l = l[0]
min_l = l[n-1]
max_idx = 0
min_idx = n-1
for i in range(n):
    if l[i] > max_l:
        max_l = l[i]
        max_idx = i
    if l[i] <= min_l:
        min_l = l[i]
        min_idx = i
if max_idx > min_idx:
    print(max_idx + n - 2 - min_idx)
else:
    print(max_idx + n - 1 - min_idx)
