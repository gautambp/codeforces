s = input().strip()
if len(s) <= 2:
    print(0)
else:
    s = s[1:-1].split(',')
    d = {ch.strip() for ch in s }
    print(len(d))