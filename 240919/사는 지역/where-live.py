class info:
    def __init__(self, name, address, street):
        self.name = name
        self.address = address
        self.street = street


n = int(input())

infos = []

for _ in range(n):
    arr = input().split()
    i = info(arr[0], arr[1], arr[2])
    infos.append(i)

i = infos[n-1]
print(f"name {i.name}")
print(f"addr {i.address}")
print(f"city {i.street}")