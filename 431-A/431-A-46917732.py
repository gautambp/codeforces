a = [int(i) for i in input().strip().split(' ')]
total = 0
for ch in input().strip():
    total += a[int(ch)-1]
print(total)