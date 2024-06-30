n, q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    que = list(map(int, input().split()))
    
    if(que[0] == 1):
        print(arr[que[1] - 1])
    elif(que[0] == 2):
        for i in range(len(arr)):
            if(arr[i] == que[1]):
                print(i + 1)
                break
            
            if(i == len(arr) - 1):
                print(0)
    elif(que[0] == 3):
        for i in range(que[1], que[2] + 1):
            print(arr[i - 1], end=' ')
        print()