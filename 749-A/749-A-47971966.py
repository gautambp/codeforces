n = int(input())
three_cnt = (1 if n%2 == 1 else 0)
two_cnt = n//2
if three_cnt > 0:
    two_cnt -= 1
print(two_cnt+three_cnt)
print('2 '*two_cnt, end='')
if three_cnt > 0:
    print('3')