n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

isTrue = False

for i in range(n1 - n2 + 1):
    for j in range(len(arr2)):
        if(arr1[i+j] != arr2[j]):
            break
        if(j == len(arr2) -1):
            isTrue = True

if(isTrue):
    print("Yes")
else:
    print("No")