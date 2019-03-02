s = input().split()
n = int(s[0])
m = int(s[1])
b = False
for i in range(n):
    if i%2 == 0:
        print('#'*m)
    else:
        s = '.'*(m-1)
        print(('#' + s if b else s + '#'))
        b = not b