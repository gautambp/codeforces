d = {}
org_kb = input()
new_kb = input()
m = input()
for i in range(26):
    d[org_kb[i]] = new_kb[i]
for ch in m:
    if ch.lower() in d:
        new_ch = d[ch.lower()]
        print((new_ch if ch.islower() else new_ch.upper()), end='')
    else:
        print(ch, end='')