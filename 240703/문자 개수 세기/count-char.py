string = input()
aph = input()

cnt = 0

for i in range(len(string)):
    if(ord(string[i]) == ord(aph)):
        cnt += 1

print(cnt)