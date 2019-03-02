s = input().split()
a, b = int(s[0]), int(s[1])
an = int(a ** 0.5)
bn = int(b ** (1/3))
while True:
    if bn*(bn+1) == b:
        break
    elif bn*(bn+1) > b:
        bn -= 1
        break
    bn += 1
print('Vladik' if an <= bn else 'Valera')