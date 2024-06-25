a, b = map(int, input().split())

tf = False

for i in range(a, b+1):
    if(1920 % i == 0 and 2880 % i == 0):
        tf = True
        break

if (tf == True):
    print(1)
else:
    print(0)