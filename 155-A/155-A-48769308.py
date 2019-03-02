n = int(input())
min_s = None
max_s = None
cnt = 0
for s in input().split():
    if min_s == None:
        min_s = int(s)
    if max_s == None:
        max_s = int(s)
    if min_s > int(s):
        min_s = int(s)
        cnt += 1
    elif max_s < int(s):
        max_s = int(s)
        cnt += 1
print(cnt)