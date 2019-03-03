import heapq

nks = input().split()
n = int(nks[0])
k = int(nks[1])
c = list(map(int, input().split()))
s = input()
t_cost = 0
last_ch = s[0]
ch_len = 0
ch_l = []
i = 0
while i <= n:
    if i < n and s[i] == last_ch:
        ch_len += 1
        heapq.heappush(ch_l, c[i])
    else:
        t_cost += sum(ch_l)
        while ch_len > k:
            t_cost -= heapq.heappop(ch_l)
            ch_len -= 1
        if i < n:
            last_ch = s[i]
            ch_l = [c[i]]
            ch_len = 1
    i += 1
print(t_cost)
