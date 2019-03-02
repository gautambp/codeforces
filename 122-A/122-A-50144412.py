n = int(input())
print('YES' if any([n%i == 0 for i in [4,7,44,47,74,77,444,447,474,744,477,747,774,777]]) else 'NO')