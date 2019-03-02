n = int(input())
s = input().strip()
total = 0
while s.find('xxx') >= 0:
    s = s.replace('xxx', 'xx', 1)
    total += 1
print(total)