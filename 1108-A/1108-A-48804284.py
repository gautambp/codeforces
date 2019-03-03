for _ in range(int(input())):
    l1, r1, l2, r2 = list(map(int, input().split()))
    lr1 = (l1 + r1)//2
    lr2 = (l2 + r2)//2
    if lr1 == lr2:
        if lr1 == l1:
            lr1 += 1
        else:
            lr1 -= 1
    print('{} {}'.format(lr1, lr2))
