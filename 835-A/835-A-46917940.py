(s, v1, v2, t1, t2) = [int(i) for i in input().strip().split(' ')]
total1 = t1 + s*v1 + t1
total2 = t2 + s*v2 + t2
if total1 < total2:
    print('First')
elif total2 < total1:
    print('Second')
else:
    print('Friendship')