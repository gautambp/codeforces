n = int(input())
l = list(map(int, input().split()))
b_sum = c_sum = 0
for i in l:
    if i <= 0:
        c_sum += i
    else:
        b_sum += i
print(b_sum-c_sum)
