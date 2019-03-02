def decodeString(s, n, d):
    if n == 1: return s
    if d == n: return s[::-1]
    if n%d != 0: return decodeString(s, n, d+1)
    s1 = s[:d]
    s = s1[::-1] + s[d:]
    return decodeString(s, n, d+1)
    
n = int(input()) 
s = input()
print(decodeString(s, n, 2))