class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())

p = []

for _ in range(n):
    arr = input().split()
    p.append(People(arr[0], int(arr[1]), int(arr[2])))

p.sort(key=lambda x:(x.height, -x.weight))

for i in range(n):
    pp = p[i]
    print(pp.name, pp.height, pp.weight)