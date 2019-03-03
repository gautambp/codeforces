s = input()
g = [0]*4

def placeVerTile(c):
    for i in [0, 3, 1, 2]:
        if g[0][i] == 0 and g[1][i] == 0:
            g[0][i] = c
            g[1][i] = c
            return (0,i)
        if g[2][i] == 0 and g[3][i] == 0:
            g[2][i] = c
            g[3][i] = c
            return (2,i)
    for i in [0, 3, 1, 2]:
        if g[1][i] == 0 and g[2][i] == 0:
            g[1][i] = c
            g[2][i] = c
            return (1,i)
    return (None, None)

def placeHorTile(c):
    for i in [0, 3, 1, 2]:
        if g[i][0] == 0 and g[i][1] == 0:
            g[i][0] = c
            g[i][1] = c
            return (i, 0)
        if g[i][2] == 0 and g[i][3] == 0:
            g[i][2] = c
            g[i][3] = c
            return (i, 2)
    for i in [0, 3, 1, 2]:
        if g[i][1] == 0 and g[i][2] == 0:
            g[i][1] = c
            g[i][2] = c
            return (i, 1)
    return (None, None)

def clearGrid():
    for i in range(4):
        if g[i][0] != 0 and g[i][1] != 0 and g[i][2] != 0 and g[i][3] != 0:
            g[i][0] = 0
            g[i][1] = 0
            g[i][2] = 0
            g[i][3] = 0
        if g[0][i] != 0 and g[1][i] != 0 and g[2][i] != 0 and g[3][i] != 0:
            g[0][i] = 0
            g[1][i] = 0
            g[2][i] = 0
            g[3][i] = 0
    
for i in range(4):
    g[i] = [0]*4
cnt = 1
for ch in s:
    p = None
    if ch == '0':
        p = placeVerTile(cnt)
    else:
        p = placeHorTile(cnt)
    clearGrid()
    if p == None or p[0] == None:
        break
    print('{} {}'.format(p[0]+1, p[1]+1))
