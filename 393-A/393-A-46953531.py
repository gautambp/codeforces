import math

s = 'nineteenineteenineteenineteenineteenineteenineteenineteenineteenineteenineteenineteenineteen'
s = input().strip()
s_len = len(s)
s_occ = {'i':1, 'e':3, 't':1, 'n':3}
min_occ = s_len
for c in s_occ:
    cnt = s.count(c)
    if c == 'n' and cnt > 3:
        cnt_inc = int(cnt/3)
        cnt += cnt_inc + int(cnt_inc/3)
    occ = int(cnt/s_occ[c])
    #print('{} {} {}'.format(c, cnt, occ))
    if occ < min_occ:
        min_occ = occ
print(min_occ)