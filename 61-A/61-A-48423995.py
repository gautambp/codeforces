s1 = input()
s2 = input()
for ch1, ch2 in zip(s1, s2):
    print(('1' if int(ch1) + int(ch2) == 1 else '0'), end='')