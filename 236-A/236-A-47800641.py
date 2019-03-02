s = input()
d = {}
for ch in s:
    d[ch] = ch
print('IGNORE HIM!' if len(d)%2 != 0 else 'CHAT WITH HER!')