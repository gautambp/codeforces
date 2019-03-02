m_sum = 0
n = int(input())
n_half = int(n/2)
for i in range(n):
    e = [int(i) for i in input().strip().split(' ')]
    if i == n_half:
        m_sum += sum(e)
    else:
        m_sum += e[i]
        m_sum += e[n-i-1]
        m_sum += e[n_half]
print(m_sum)