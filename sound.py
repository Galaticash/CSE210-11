DEFAULT_VOLUME = 1.0

class Sound():
    """
        A type of object that holds the filepath and volume of a sound to be played.
    """
    def __init__(self, filename, volume = DEFAULT_VOLUME):
        self._filename = filename
        # NOTE: Volume is currently not used
        self._volume = volume

    def get_filename(self):
        """
            Returns the sound's filename (filepath assumed assets\\sounds\\filename)
        """
        return self._filename

    def get_volume(self):
        """
            Returns the volume of the sound (a float between 0 and 1.0)
        """
        return self._volume