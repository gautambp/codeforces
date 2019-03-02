def isPrime(n):
    if n == 2 or n == 3 or n == 5:
        return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False
    for i in range(7, int(n ** 0.5)+1, 2):
        if n%i == 0:
            return False
    return True

n = int(input())
a = n//2
b = n-a
while True:
    if isPrime(a):
        a -= 1
        b += 1
    elif isPrime(b):
        a -= 1
        b += 1
    else:
        break
print('{} {}'.format(a,b))