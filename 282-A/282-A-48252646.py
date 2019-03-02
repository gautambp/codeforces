r = range(int(input().strip()))
X = 0
for _ in r:
    if input().find('++') >= 0:
        X += 1
    else:
        X -= 1
print(X)