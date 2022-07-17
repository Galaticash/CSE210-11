from actors.message import Message
from color import Color
from actors.image import Image

COUNTER_IMAGE_SCALE = 2

class Counter(Message):
    """
        A type of Message that counts
    """
    def __init__(self, position, font_size, message, image_file = "", color="WHITE"):
        super().__init__(position, font_size, message, color)
        self._color = Color("WHITE")
        self._count = 0
        self._image = Image(image_file, COUNTER_IMAGE_SCALE)
        # If there is an image, then display that
        self._display_image = not image_file == ""

    def has_image(self):
        return self._display_image

    def reset_count(self):
        """
            Resets the point count to 0.
        """
        self._count = 0

    def add(self, points):
        """
            Adds or removes points from the count.
        """
        self._count += points

    def set_count(self, points):
        """
            Resets the count and sets it to the given number of points.
        """
        self.reset_count()
        self.add(points)

    def get_image(self):
        """
            Returns the image associated with the Counter.
        """
        return self._image

    def get_count(self):
        """
            Returns the integer Score.
        """
        return self._count

    def get_display(self):
        """
            Returns the count as a single string.
        """
        if self._display_image:
            return self.get_image()
        else:
            return f"{self._message} {self._count}"