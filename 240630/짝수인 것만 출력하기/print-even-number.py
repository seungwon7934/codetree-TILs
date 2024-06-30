n = int(input())
all_arr = list(map(int, input().split()))

even_arr = list()

for num in all_arr:
    if(num % 2 == 0):
        even_arr.append(num)

for num in even_arr:
    print(num, end=' ')