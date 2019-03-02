def isPalindrom(s):
    s_len = len(s)
    if s_len == 1:
        return (True, 0)
    else:
        mid_pt = s_len // 2
        for i in range(mid_pt):
            if s[i] != s[s_len-i-1]:
                return (False, i)
        return (True, 0)
    
s = list(input())
is_palin, idx = isPalindrom(s)
while not is_palin:
    s.insert(len(s)-idx, s[idx]);
    is_palin, idx = isPalindrom(s)
    
print(''.join(s))