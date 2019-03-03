for _ in range(int(input())):
    s,a,b,c = list(map(int, input().split()))
    no_ch = s // c
    no_ch += b * (no_ch // a)
    print(no_ch)
