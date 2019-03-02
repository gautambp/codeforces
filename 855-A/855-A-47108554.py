name_l = []
for _ in range(int(input())):
    n = input()
    if n not in name_l:
        print('NO')
        name_l.append(n)
    else:
        print('YES')