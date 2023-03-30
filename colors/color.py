class Color:
    def __init__(self, code: int):
        self.code = code
        self.ansi = f"\x1b[38;5;{code}m"
        self.rgb = Color.get_rgb(code)

    @staticmethod
    def get_rgb(color_code: int):
        fixed_code = color_code - 15
        red_value = fixed_code // 36
        green_value = (fixed_code % 36) // 6
        blue_value = (fixed_code % 36) % 6
        return [red_value, green_value, blue_value]

    @staticmethod
    def from_rgb(rgb: list[int]):
        return Color(16 + rgb[0] * 36 + rgb[1] * 6 + rgb[2])
