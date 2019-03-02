s1 = input()
s2 = input()
s3 = input()
if sorted(s1+s2) == sorted(s3):
    print('YES')
else:
    print('NO')