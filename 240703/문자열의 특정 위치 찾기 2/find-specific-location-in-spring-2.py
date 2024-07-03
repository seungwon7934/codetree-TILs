arr = [ "apple", "banana", "grape", "blueberry", "orange"]
aph = input()
cnt = 0

for i in range(len(arr)):
        if(arr[i][2] == aph or arr[i][3] == aph):
            cnt += 1
            print(arr[i])
print(cnt)