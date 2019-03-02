n = int(input())
#(n, h) = [int(i) for i in input().strip().split(' ')]
a = list(map(int, input().strip().split(' ')))
print(sum(a)/len(a))