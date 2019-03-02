(n,p,k) = [int(i) for i in input().strip().split(' ')]
if p-k > 1:
    print('<<', end=' ')
for i in range(p-k, p+k+1):
    if i < 1: continue
    if i > n: continue
    if i == p:
        print('(' + str(i) + ')', end=' ')
    else:
        print(i, end=' ')
if p+k < n:
    print('>>', end=' ')
print('')