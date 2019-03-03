y,b,r = list(map(int,input().split()))
val = 0
if r <= b and r <= y:
    val = r + (r-1) + (r-2)
elif b <= r and b <= y:
    if r > b:
        val = b + b+1 + b-1
    else:
        val = b-1 + b + b-2
else:
    if r == y+1:
        val = y-1 + y + y+1
    else:
        val = y + y+1 + y+2
print(val)
