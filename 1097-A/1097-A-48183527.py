c = input()
l = input().split()
print('YES' if sum([1 for i in l if i[0] == c[0] or i[1] == c[1]]) > 0 else 'NO')
