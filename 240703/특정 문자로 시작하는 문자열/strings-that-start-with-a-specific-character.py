n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

aph = input()
cnt = 0
length = 0

for i in range(len(arr)):
    if(arr[i][0] == aph):
        cnt += 1
        length += len(arr[i])

print(f"{cnt} {length / cnt:.2f}")