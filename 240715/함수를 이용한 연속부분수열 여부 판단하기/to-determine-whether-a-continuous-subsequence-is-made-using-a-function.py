def isTrue(arr1, arr2):
    for i in range(len(arr1) - len(arr2) + 1):
        if arr1[i:i + len(arr2)] == arr2:
            return True
    return False

l1, l2 = map(int, input().split())

arr1 = list(input().split())
arr2 = list(input().split())

if isTrue(arr1, arr2):
    print("Yes")
else:
    print("No")