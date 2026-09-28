"""Make a pixel-art alien head as alien.bmp for the game sprite."""
from PIL import Image

# 16x16 pixel-art grid, 1 char = 1 pixel
# . = transparent-ish black, G = green, W = white (eye), B = black (pupil)
GRID = """
....GGGGGGGG....
..GGGGGGGGGGGG..
.GGGGGGGGGGGGGG.
GGGGGGGGGGGGGGGG
GGGWWGGGGGGWWGGG
GGWWWWGGGGWWWWGG
GGWWBWGGGGWWBWGG
GGGWWGGGGGGWWGGG
GGGGGGGGGGGGGGGG
GGGGGCCCCGGGGGGG
GGGGCCCCCCGGGGGG
GGGGGGGGGGGGGGGG
.GGGGGGGGGGGGGG.
..GGGGGGGGGGGG..
....GGGGGGGG....
................
""".strip("\n").splitlines()

COLORS = {".": (0, 0, 0), "G": (57, 255, 20), "C": (30, 150, 10),
          "W": (255, 255, 255), "B": (0, 0, 0)}

img = Image.new("RGB", (16, 16))
for y, row in enumerate(GRID):
    for x, ch in enumerate(row):
        img.putpixel((x, y), COLORS[ch])

img.save("images/alien.bmp")
print("saved images/alien.bmp")
