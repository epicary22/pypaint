import time

for code in range(256):
    print(f"\033[38;5;{code}m{code}\t", end="")
    if (code - 15) % 6 == 0 and code != 0 or code % 6 == 0 and code <= 15 and code != 0:
        print()

# for color_to_check in range(1, 37):
#     for code in range(255):
#         if (code - 15) % 36 == color_to_check and code > 15 and code < 232:
#             print(f"\033[38;5;{code}m{code}", end=" ")
#     print()
#     if color_to_check % 6 == 0:
#         time.sleep(1)
#         print("\033[2J")

def generate_color_palettes(code):
    red_palette = [((code - 16) % 36) + 16 + (36 * i) for i in range(6)]
    green_base = 16 + 36 * ((code - 16) // 36)
    green_palette = [green_base + ((code - green_base) % 6) + (6 * i) for i in range(6)]
    blue_base = green_base + ((code - green_base) // 6) * 6
    blue_palette = [blue_base + i for i in range(6)]
    return [red_palette, green_palette, blue_palette]

def find_color_makeups(code):
    # Red, then green, then blue
    return [(code - 16) // 36, (code % 36) // 6, (code % 36) % 6]

def decode_color_makeups(color_makeups):
    return color_makeups[0] * 36 + color_makeups[1] * 6 + color_makeups[2]

print("\033[0m")
brush = input("Choose brush: ")
color_code = int(input("Choose color code: "))
print(f"\033[38;5;{color_code}m", *([brush*10]*10), sep="\n")
for palette in generate_color_palettes(color_code):
    for palette_code in palette:
        print(f"\033[38;5;{palette_code}m{brush}", end="")
    print()

cm = find_color_makeups(color_code)
print(cm, decode_color_makeups(cm))

