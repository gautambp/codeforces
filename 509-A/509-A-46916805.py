n = int(input())

def getMatrixVal(i, j):
    if i == 1 or j == 1: return 1
    return getMatrixVal(i-1, j) + getMatrixVal(i, j-1)

print(getMatrixVal(n, n))