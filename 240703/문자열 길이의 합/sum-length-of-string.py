n = int(input())

arr = []
cnt = 0
length = 0

for _ in range(n):
    string = input()
    if(string[0] == 'a'):
        cnt += 1
    length += len(string)

print(length, cnt)