a, b = map(int, input().split())

if(a < 90):
    print(0)
else:
    print(100000) if b >= 95 else print(50000) if b >= 90 else print(0)