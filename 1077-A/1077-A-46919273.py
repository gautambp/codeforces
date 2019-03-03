import math

for _ in range(int(input())):
    (a, b, k) = [int(i) for i in input().strip().split(' ')]
    print(math.ceil(k/2)*a - int(k/2)*b)
    
