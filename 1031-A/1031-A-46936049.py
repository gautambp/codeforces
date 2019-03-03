(w,h,k) = [int(i) for i in input().strip().split(' ')]
total = 0
for i in range(k):
    total += 2 * ((w-4*i) + (h-4*i)) - 4
print(total)
