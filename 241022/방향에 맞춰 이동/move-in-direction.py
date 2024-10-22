x, y = 0, 0
N = int(input())

for _ in range(N):
    d, m = input().split()
    m = int(m)

    if(d == "N"):
        y += m
    
    if(d == "E"):
        x += m

    if(d == "S"):
        y -= m
    
    if(d == "W"):
        x -= m
    
print(x, y)