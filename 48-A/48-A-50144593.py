w = {
     ('rock', 'scissors'): True,
     ('scissors', 'rock'): False,
     ('paper', 'rock'): True,
     ('rock', 'paper'): False,
     ('scissors', 'paper'): True,
     ('paper', 'scissors'): False     
}
f = input()
m = input()
s = input()
if (f, m) in w and w[(f, m)] and (f, s) in w and w[(f, s)]:
    print('F')
elif (m, f) in w and w[(m, f)] and (m, s) in w and w[(m, s)]:
    print('M')
elif (s, m) in w and w[(s, m)] and (s, f) in w and w[(s, f)]:
    print('S')
else:
    print('?')