s = input()
s_len = len(s)
l_cnt = sum([1 for c in s if c.islower()])
u_cnt = s_len-l_cnt
if l_cnt >= u_cnt:
    print(s.lower())
else:
    print(s.upper())