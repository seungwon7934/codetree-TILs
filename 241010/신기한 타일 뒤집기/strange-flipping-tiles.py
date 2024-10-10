from dataclasses import dataclass

@dataclass
class tile:
    x: int
    color: str


n = int(input())
idx = 1000000
tiles = {}
w = b = 0

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if(d == "L"):
        for i in range(idx, idx - x, -1):
            if(i not in tiles):
                tiles[i] = tile(i, "w")
            else:
                tiles[i].color = "w"
        idx = idx - (x - 1)
    else:
        for i in range(idx, idx + x):
            if(i not in tiles):
                tiles[i] = tile(i, "b")
            else:
                tiles[i].color = "b"
        idx = idx + (x - 1)

for i in tiles:
    if(tiles[i].color == "w"):
        w += 1
    else:
        b += 1

print(w, b)