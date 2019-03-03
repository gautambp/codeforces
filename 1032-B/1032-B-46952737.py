import math

s = 'iHufyYRNbXpCmShignQspDPfOpHsTJImVaShhpEsfLcTJushZgoeq'
s = input().strip()
s_len = len(s)
s_r = 0
s_c = 0
a_cnt = 0
for c in range(20, 0, -1):
    r = math.ceil(s_len/c)
    a_cnt = abs(r*c - s_len)
    if a_cnt < r:
        s_r = r
        s_c = c
        while a_cnt > 0:
            s = s[:a_cnt*c+1] + '*' + s[a_cnt*c+1:]
            a_cnt -= 1
        break
print('{} {}'.format(s_r, s_c))
for r in range(s_r):
    print(s[r*s_c:(r+1)*s_c])
