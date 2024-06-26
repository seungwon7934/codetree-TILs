n = int(input())

1 - 3
2 - 5
3 - 7

for i in range(n * 2 + 1):

    if((i + 1) % 2 != 0):
        for j in range(n * 2 + 1):
            print("* ", end='')
        print()
    else:
        for j in range(n * 2 + 1):
            if (j % 2 != 0):
                print("  ", end='')
            else:
                print("* ", end='')
        print()