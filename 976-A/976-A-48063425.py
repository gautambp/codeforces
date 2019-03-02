n = int(input())
s = input()
if s == '0':
    print(s)
else:
    cnt = s.count('0')
    print('1' + '0'*cnt)