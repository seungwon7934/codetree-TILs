a, b, c = map(int, input().split())

if(b < 11):
    print(-1)
elif(b == 11 and c < 11):
    print(-1)
else:
    d = 11 - a
    h = 24 * d - abs(11 - b)
    m = 60 * h - abs(11 - c)
    print(abs(m))