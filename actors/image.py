from pyray import Color
from constants import HARD_COLORS

class Image():
    def __init__(self, filepath, scale = 1, rotation = 0, tint = Color(HARD_COLORS["WHITE"][0], HARD_COLORS["WHITE"][1], HARD_COLORS["WHITE"][2], HARD_COLORS["WHITE"][3])):
        self._filepath = "assets\\" + str(filepath)
        self._tint = tint
        self._scale = scale
        self._rotation = rotation

    def get_filepath(self):
        """
            Returns the filepath of the Image.
        """
        return self._filepath

    def get_tint(self):
        """
            Returns the tuple Color to display the image.
        """
        return (self._tint.r, self._tint.g, self._tint.b, self._tint.a)

    def get_scale(self):
        return self._scale

    def get_rotation(self):
        return self._rotation