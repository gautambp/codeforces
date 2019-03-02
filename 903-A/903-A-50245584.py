def isValidTotal(n):
    if n < 0: return False
    if n == 0 or n%3 == 0 or n%7 == 0: return True
    return isValidTotal(n-3) or isValidTotal(n-7)

for _ in range(int(input())):
    n = int(input())
    print('YES' if isValidTotal(n) else 'NO')