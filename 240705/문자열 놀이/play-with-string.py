s, q = input().split()

arr = list(s)

for _ in range(int(q)):
    que = input().split()
    if(que[0] == '1'):
        temp = arr[int(que[1])-1]
        arr[int(que[1])-1] = arr[int(que[2])-1]
        arr[int(que[2])-1] = temp
    else:
        for i in range(len(arr)):
            if(arr[i] == que[1]):
                arr[i] = que[2]
    print(''.join(arr))