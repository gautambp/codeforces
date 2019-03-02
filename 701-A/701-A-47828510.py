n = int(input())
l = list(map(int, input().split()))
l_sum = sum(l)
p_sum = 2*l_sum//n
d = [None]*101
for i in range(n):
    c_diff = p_sum-l[i]
    if d[c_diff] == None or len(d[c_diff]) == 0:
        if d[l[i]] == None:
            d[l[i]] = [i]
        else:
            d[l[i]].append(i)
    else:
        idx = d[c_diff].pop()
        print(i+1, idx+1)