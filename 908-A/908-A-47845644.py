s = input()
vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for c in s:
    if c.isalpha():
        if c in vowels:
            cnt += 1
    elif c.isdigit():
        d = int(c)
        if d%2 != 0:
            cnt += 1
print(cnt)