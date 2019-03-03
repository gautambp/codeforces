(ns, ks) = input().split(' ')
n = int(ns)
k = int(ks)
a = [None]*n
a_str = input().split(' ')
for i in range(n):
    a[i] = int(a_str[i])
a = sorted(a)

sub_amt = 0
cnt = 0
l = 0
while cnt < k:
    if l >= n:
        print(0)
        cnt += 1
    else:
        a[l] -= sub_amt
        if a[l] <= 0:
            pass
        else:
            min_a = a[l]
            print(min_a)
            cnt += 1
            sub_amt += min_a
        l += 1
