n = int(input())
s = input().strip()
sa = s.count('A')
sd = s.count('D')
if sd > sa:
    print('Danik')
elif sa > sd:
    print('Anton')
else:
    print('Friendship')