arr = [0] * 5

for i in range(5):
    arr[i] = int(input())

tf = True

for i in range(5):
    if(arr[i] % 3 != 0):
        tf = False
        break

if(tf == True):
    print(1)
else:
    print(0)