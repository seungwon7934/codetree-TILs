a, b, c = map(int, input().split())

if a <= b and a >= c or a <= c and a >= b:
    print(a)
if b <= a and b >= c or b <= c and b >= a:
    print(b)
if c <= b and c >= a or c <= a and c >= b:
    print(c)