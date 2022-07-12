class Image():
    def __init__(self, filepath, scale = 1, rotation = 0):
        self._filepath = "assets\\" + filepath
        self._scale = scale
        self._rotation = rotation

    def get_filepath(self):
        return self._filepath

    def get_scale(self):
        return self._scale

    def get_rotation(self):
        return self._rotation