class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

p = []

for _ in range(n):
    arr = input().split()
    p.append(People(arr[0], arr[1], arr[2]))

p.sort(key=lambda x:x.height)

for q in p:
    print(q.name, q.height, q.weight)