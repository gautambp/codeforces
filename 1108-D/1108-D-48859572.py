n = int(input())
last_idx = n-1
s = input()
c_map = {'R': 'G', 'G': 'B', 'B': 'R'}
c_idx = {'R': 0, 'G': 1, 'B': 2}
new_s = ['']*n
cnt = 0
i = 1
while i < last_idx:
    if s[i-1] == s[i] and s[i] == s[i+1]:
        new_s[i] = c_map[s[i]]
        new_s[i+1] = s[i+1]
        i += 1
        cnt += 1
    elif s[i-1] == s[i]:
        new_ch_idx = 3 - (c_idx[s[i]] + c_idx[s[i+1]])
        new_s[i] = ('R' if new_ch_idx == 0 else 'G' if new_ch_idx == 1 else 'B')
        cnt += 1
    else:
        new_s[i] = s[i]
    i += 1

if n > 1:
    if s[0] == new_s[1]:
        new_s[0] = c_map[new_s[1]]
        cnt += 1
    else:
        new_s[0] = s[0]
    if s[last_idx] == new_s[last_idx-1]:
        new_s[last_idx] = c_map[new_s[last_idx-1]]
        cnt += 1
    else:
        new_s[last_idx] = s[last_idx]
    print(cnt)
    print(''.join(new_s))
else:
    print(0)
    print(s)
