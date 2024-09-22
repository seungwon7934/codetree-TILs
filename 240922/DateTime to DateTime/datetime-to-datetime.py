a, b, c = map(int, input().split())

if(a == 11 and b < 11):
    print(-1)
elif(b == 11 and c < 11):
    print(-1)
else:
    d = a - 11
    h = 24 * d + (b - 11)
    m = 60 * h + (c - 11)
    print(m)