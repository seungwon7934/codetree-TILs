x = 0
y = 0

n = int(input())

for _ in range(n):
    a, b = input().split()
    b = int(b)
    if(a == 'N'):
        y += b
    elif(a == 'E'):
        x += b
    elif(a == 'S'):
        y -= b
    else:
        x -= b

print(x, y)