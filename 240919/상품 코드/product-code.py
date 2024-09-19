class Goods:
    def __init__(self, name = "codetree", code = 50):
        self.name = name
        self.code = code

arr = input().split()

p1 = Goods()
p2 = Goods(arr[0], int(arr[1]))

print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")