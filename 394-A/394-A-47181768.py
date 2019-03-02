s = input().strip()
(l, r) = s.split('=')
a_b = len(r)
a = len(l.split('+')[0])
b = len(l.split('+')[1])
is_possible = True
if a+b == a_b-2:
    a += 1
    a_b -= 1
elif a+b == a_b+2:
    if a > b: a -= 1
    else: b -= 1
    a_b += 1
elif a+b != a_b:
    is_possible = False
if is_possible:
    print('|'*a + '+' + '|'*b + '=' + '|'*a_b)
else:
    print('Impossible')