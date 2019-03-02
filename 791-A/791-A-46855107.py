#(ls, bs) = '4 7'.strip().split(' ')
(ls, bs) = input().strip().split(' ')
l = int(ls)
b = int(bs)
n = 0
while True:
    n += 1
    l = l*3
    b = b*2
    if l > b:
        print(n)
        break