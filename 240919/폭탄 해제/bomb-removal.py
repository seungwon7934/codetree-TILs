class bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

arr = input().split()

b = bomb(arr[0], arr[1], arr[2])

print(f"code : {b.code}\ncolor : {b.color}\nsecond : {b.second}")