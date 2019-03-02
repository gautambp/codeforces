n = int(input())
l = list(map(int, input().split()))
s_sum = 0
o_sum = 0
is_s_turn = True
while len(l) > 0:
    if l[0] > l[len(l)-1]:
        if is_s_turn:
            s_sum += l.pop(0)
        else:
            o_sum += l.pop(0)
    else:
        if is_s_turn:
            s_sum += l.pop(len(l)-1)
        else:
            o_sum += l.pop(len(l)-1)
    is_s_turn = not is_s_turn
print('{} {}'.format(s_sum, o_sum))