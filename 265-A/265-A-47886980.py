s = input()
t = input()
s_idx = 0
t_idx = 0
while s_idx < len(s) and t_idx < len(t):
    if s[s_idx] == t[t_idx]:
        s_idx += 1
    t_idx += 1
print(s_idx+1)