arr = []

for _ in range(10):
    arr.append(input())

aph = input()

for i in range(len(arr)):
    if(arr[i][len(arr[i]) - 1] == aph):
        print(arr[i])