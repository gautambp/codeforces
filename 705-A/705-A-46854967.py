n = 3
n = int(input())
is_hate = True
while n > 0:
    if is_hate:
        print('I hate ', end='')
    if not is_hate:
        print('I love ', end='')
    if n > 1:
        print('that ', end='')
    else:
        print('it ', end='')
    n -= 1
    is_hate = not is_hate
print('')