s = input()
f_cnt = s.count('4')
s_cnt = s.count('7')
print('YES' if f_cnt+s_cnt == 4 or f_cnt+s_cnt == 7 else 'NO')
