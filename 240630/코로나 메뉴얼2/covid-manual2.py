A = 0
B = 0
C = 0
D = 0

for _ in range(3):
    arr = list(input().split())
    if(arr[0] == 'Y'):
        if(int(arr[1]) >= 37):
            A += 1
        else:
            C += 1
    elif(arr[0] == 'N'):
        if(int(arr[1]) >= 37):
            B += 1
        else:
            D += 1
    
print(A, B, C, D, end=' ')

if(A >= 2):
    print("E")