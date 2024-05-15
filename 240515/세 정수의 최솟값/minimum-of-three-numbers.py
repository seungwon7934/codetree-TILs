a, b, c = map(int, input().split())

print(a) if(a <= b and a <= c) else print(b) if(b <= a and b <= c) else print(c)