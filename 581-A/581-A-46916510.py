(a, b) = [int(i) for i in input().strip().split(' ')]
ab_min = a
ab_same = int((b - a)/2)
if b < a:
    ab_min = b
    ab_same = int((a - b)/2)
print('{} {}'.format(ab_min, ab_same))


