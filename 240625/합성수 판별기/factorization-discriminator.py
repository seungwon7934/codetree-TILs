n = int(input())

tf = False

for i in range(2, n):
    if(n % i == 0):
        tf = True
        break

if(tf == True):
    print("C")
else:
    print("N")