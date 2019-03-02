from itertools import combinations 

s = input()
s = ''.join(c for c in s if c == 'A' or c == 'Q')
cnt = 0
for i in combinations(s, 3):
    cnt += (1 if i[0] == 'Q' and i[1] == 'A' and i[2] == 'Q' else 0)
print(cnt)