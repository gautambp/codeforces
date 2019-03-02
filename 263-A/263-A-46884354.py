r = 0
c = 0
for i in range(5):
    l = input().strip().split(' ')
    for j in range(5):
        if l[j] == '1':
            r = i+1
            c = j+1
print(abs(r-3) + abs(c-3))