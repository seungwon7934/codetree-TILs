a, b = map(int, input().split())

total = 0
if(b > a):
    temp = a
    a = b
    b = temp
for i in range(a, b+1):
    if(i % 5 == 0):
        total += i

print(total)