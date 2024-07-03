arr = []

for _ in range(10):
    arr.append(input())

aph = input()
cnt = 0

for i in range(len(arr)):
    if(arr[i][len(arr[i]) - 1] == aph):
        cnt += 1
        print(arr[i])

if(cnt == 0):
    print("None")