n = 3
n = int(input())
ans = '0 0 1'.split(' ')
ans = input().strip().split(' ')
if any(map(lambda x: x == '1', ans)):
    print('HARD')
else:
    print('EASY')
