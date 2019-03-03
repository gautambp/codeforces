def findColorChange(n, s, idx):
    cnt = 0
    for i in range(n):
        if s[i] == 'R' and i%3 != idx[0]: cnt += 1
        if s[i] == 'G' and i%3 != idx[1]: cnt += 1
        if s[i] == 'B' and i%3 != idx[2]: cnt += 1
    return cnt
    
n = int(input())
s = input()
cnt = 0
if n == 1:
    print(0)
    print(s)
elif n == 2:
    if s[0] == s[1]:
        print(1)
        print('R'+s[1] if s[0] != 'R' else 'G'+s[1] if s[1] != 'G' else 'B'+s[1])
    else:
        print(0)
        print(s)
else:
    idx = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    #idx_s = ['RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR']
    min_val = None
    min_idx = None
    for i in range(len(idx)):
        cnt = findColorChange(n, s, idx[i])
        if min_val == None or cnt < min_val:
            min_val = cnt
            min_idx = idx[i]
    print(min_val)
    if min_val == 0:
        print(s)
    else:
        new_s = ''
        for i in range(n):
            if s[i] == 'R':
                if i%3 != min_idx[0]: 
                    new_s += ('G' if i%3 == min_idx[1] else 'B')
                else:
                    new_s += 'R'
            if s[i] == 'G':
                if i%3 != min_idx[1]: 
                    new_s += ('R' if i%3 == min_idx[0] else 'B')
                else:
                    new_s += 'G'
            if s[i] == 'B':
                if i%3 != min_idx[2]: 
                    new_s += ('R' if i%3 == min_idx[0] else 'G')
                else:
                    new_s += 'B'
        print(new_s)
