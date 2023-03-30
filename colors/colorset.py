from colors.color import Color


class ColorSet:
    def __init__(self):
        self.colors = []

    @staticmethod
    def rgb_spectrum(rgb_index: int, color_rgb: list[int]):
        spectrum = []
        for rgb_value in range(6):
            color_rgb[rgb_index] = rgb_value
            spectrum.append(Color.from_rgb(color_rgb))
        return spectrum

    @staticmethod
    def red_spectrum(color: Color):
        return ColorSet.rgb_spectrum(0, color.rgb)
