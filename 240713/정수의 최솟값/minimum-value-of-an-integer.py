def minimun(*args):
    return min(args)
    # m = args[0]
    # for i in range(len(args)):
    #     if(m > args[i]):
    #         m = args[i]
    # return m

arr = tuple(map(int, input().split()))

print(minimun(*arr))