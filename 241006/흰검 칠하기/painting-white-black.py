class Tile:
    def __init__(self, index=0, color='none', count=0):
        self.index = index
        self.color = color
        self.count = count


n = int(input())
idx = 1000000
line = []
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if(d == "L"):
        if(len(line) == 0):
            for i in range(idx - x, idx):
                line.append(Tile(i, "w", 1))

        else:
            for i in range(idx - x, idx):
                exist = False

                for tile in line:
                    if(tile.index == i):
                        tile.color = "w"
                        tile.count += 1
                        exist = True

                if(exist == False):
                    line.append(Tile(i, "w", 1))
        idx -= x

    else:
        if(len(line) == 0):
            for i in range(idx, idx + x):
                line.append(Tile(i, "b", 1))

        else:
            for i in range(idx, idx + x):
                exist = False

                for tile in line:
                    if(tile.index == i):
                        tile.color = "b"
                        tile.count += 1
                        exist = True
                        
                if(exist == False):
                    line.append(Tile(i, "b", 1))
        idx += x

w = b = g = 0

for tile in line:
    if(tile.count >= 4):
        g += 1
    else:
        if(tile.color == "w"):
            w += 1
        else:
            b += 1

print(w, b, g)