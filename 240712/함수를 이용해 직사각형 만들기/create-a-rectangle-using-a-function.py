def draw_rect(n, m):
    for _ in range(n):
        for _ in range(m):
            print(1,end='')
        print()

n, m = map(int, input().split())

draw_rect(n, m)