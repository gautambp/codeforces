import math 
  
def gcdOfFactorial(m, n) : 
    return math.factorial(min(m, n)) 

s = input().split()  
m = int(s[0])
n = int(s[1])
print(gcdOfFactorial(m, n))