a = [[0 for j in range(2)] for i in range(3)]
e = 0

for i in range(3):
    arr = input().split()
    a[i][0] = arr[0]
    a[i][1] = int(arr[1])

for i in range(3):
    if(a[i][0] == 'Y' and a[i][1] >= 37):
        e += 1

if(e >= 2):
    print("E")
else:
    print("N")