a_ord = ord('a')

def getMinDiff(c1, c2):
    i1 = ord(c1)-a_ord
    i2 = ord(c2)-a_ord
    i1_i2 = i1 - i2
    if i1_i2 < 0: i1_i2 += 26
    i2_i1 = i2 - i1
    if i2_i1 < 0: i2_i1 += 26
    return (i1_i2 if i1_i2 < i2_i1 else i2_i1)
    
s = input()
cur_ch = 'a'
cnt = 0
for c in s:
    cnt += getMinDiff(cur_ch, c)
    cur_ch = c
print(cnt)