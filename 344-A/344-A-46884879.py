cnt = 1
last = None
for _ in range(int(input())):
    s = input()
    if last == None:
        last = s
    else:
        if last != s:
            cnt += 1
    last = s
print(cnt)