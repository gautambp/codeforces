n = int(input())
u_digit = n%10
if u_digit > 5:
    print(n+10-u_digit)
else:
    print(n-u_digit)