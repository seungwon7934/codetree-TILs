string = input()
n = int(input())

if(len(string) > n):
    for i in range(len(string) - 1, len(string) - 1 - n, -1):
        print(string[i], end='')
else:
    for i in range(len(string) - 1, -1, -1):
        print(string[i],end='')