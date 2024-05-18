arr1 = input().split()
arr2 = input().split()

age1 = int(arr1[0])
sex1 = arr1[1]

age2 = int(arr2[0])
sex2 = arr2[1]

print(1) if (age1 >= 1 and sex1 == 'M') or (age2 >= 1 and sex2 == 'M') else print(0)