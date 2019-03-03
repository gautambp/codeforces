v =  ['a','e','i','o','u']
s1 = input()
s2 = input()
if len(s1) != len(s2):
    print('No')
else:
    found = True
    for i in range(len(s1)):
        if s1[i] in v:
            if s2[i] not in v:
                found = False
                break
        elif s2[i] in v:
            found = False
            break
    print('Yes' if found else 'No')
