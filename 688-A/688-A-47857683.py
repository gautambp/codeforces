n, d = list(map(int, input().split()))
all_present = '1'*n
long_seq = 0
seq = 0
for _ in range(d):
    if input() == all_present:
        if seq > long_seq:
            long_seq = seq
        seq = 0
    else:
        seq += 1
if seq > long_seq:
    long_seq = seq
print(long_seq)