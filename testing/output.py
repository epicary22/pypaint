from colors.color import Color
from colors.colorset import ColorSet

# c = Color(190)
c = Color.from_rgb([1, 3, 2])

print(c.ansi, ":))))))))")

cs = ColorSet.red_spectrum(c)
for color in cs:
    print(color.ansi, "hi lol")
