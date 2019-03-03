s = input().split()
n = int(s[0])
m = int(s[1])
c = list(map(int, input().split()))
b = list(map(int, input().split()))
b_idx = c_idx = 0
cnt = 0
while c_idx < len(c) and b_idx < len(b):
    if b[b_idx] >= c[c_idx]:
        cnt += 1
        b_idx += 1
    c_idx += 1
    
print(cnt)
