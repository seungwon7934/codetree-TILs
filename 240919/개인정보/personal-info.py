class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

p = []

for _ in range(5):
    arr = input().split()
    p.append(People(arr[0], int(arr[1]), float(arr[2])))

p.sort(key=lambda x:(x.name))

print("name")
for pp in p:
    print(pp.name, pp.height, pp.weight)

print()

p.sort(key=lambda x:(-x.height))

print("height")
for pp in p:
    print(pp.name, pp.height, pp.weight)