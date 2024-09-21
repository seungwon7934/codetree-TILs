class S:
    def __init__(self, height, weight, index):
        self.height = height
        self.weight = weight
        self.index = index

n = int(input())
s = []
idx = 1

for _ in range(n):
    arr = input().split()
    s.append(S(int(arr[0]), int(arr[1]), idx))
    idx += 1

s.sort(key=lambda x: (x.height, -x.weight))

for i in range(n):
    ss = s[i]
    print(ss.height, ss.weight, ss.index)