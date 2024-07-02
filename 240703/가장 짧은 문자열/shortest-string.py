str1 = input()
str2 = input()
str3 = input()

arr = []
arr.append(len(str1))
arr.append(len(str2))
arr.append(len(str3))

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(abs(arr[0] - arr[len(arr) - 1]))