n = int(input())
a = [int(i) for i in input().strip().split(' ')]
a_max = max(a)
total = 0
for i in a: total += (a_max-i)
print(total)