x = int(input())
found = False
for i in range(1, x+1):
    b = i
    m = 1
    while True:
        a = b*m
        if a > x:
            break
        m += 1
        if a%b == 0 and a*b > x and a/b < x:
            print ('{} {}'.format(a, b))
            found = True
            break
    if found:
        break
if not found:
    print('-1')
