a, b = map(int, input().split())

for j in range(1, 10):
    for k in range(b, a - 1, -2):
        print(f"{k} * {j} = {k * j} ", end="")

        if(k > a):
            print("/ ", end="")
    print()