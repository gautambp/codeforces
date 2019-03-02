n = int(input())
winner = None
if n == 1:
    winner = 'Ehab'
elif n == 2:
    winner = 'Mahmoud'
else:
    if n%2 != 0:
        winner = 'Ehab'
    else:
        winner = 'Mahmoud'
print(winner)