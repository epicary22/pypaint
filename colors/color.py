class Color:
    def __init__(self, code):
        self.code = code
        self.ansi = f"\x1b[38;5;{code}m"
        self.rgb = Color.get_rgb(code)
