(n,m) = [int(i) for i in input().strip().split(' ')]
x = [int(i) for i in input().strip().split(' ')]
y = [int(i) for i in input().strip().split(' ')]
for i in x:
    if i in y:
        print(i, end=' ')
print('')