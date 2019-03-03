q = int(input())
for _ in range(q):
    d = int(input())
    ns = input()
    if d > 2 or int(ns[0]) < int(ns[1]):
        print('YES')
        print(2)
        print('{} {}'.format(ns[0], ns[1:]))
    else:
        print('NO')
