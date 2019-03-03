n = int(input())
s = (((8*n + 1) ** 0.5) - 1) / 2
print('YES' if s == int(s) else 'NO')
