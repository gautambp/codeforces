from itertools import combinations

n, d = list(map(int, input().split()))
h = list(map(int, input().split()))
cnt = 0
for i in combinations(h, 2):
    if abs(i[0]-i[1]) <= d:
        cnt += 1
print(cnt*2)