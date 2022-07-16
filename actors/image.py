from color import Color

class Image():
    def __init__(self, filepath, scale = 1, rotation = 0, tint = Color("WHITE")):
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
        return self._tint.to_tuple()

    def get_scale(self):
        return self._scale

    def get_rotation(self):
        return self._rotation