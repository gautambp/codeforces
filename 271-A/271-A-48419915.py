from collections import Counter
n = int(input())
while True:
    n += 1
    c = Counter(str(n))
    if not any(value > 1 for value in c.values()):
        print(n)
        break
