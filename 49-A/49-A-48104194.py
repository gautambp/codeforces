import string
s = input()
for i in range(len(s)-1, -1, -1):
    if s[i] in string.ascii_letters:
        print('YES' if s[i].lower() in ['a','e','i','o','u','y'] else 'NO')
        break