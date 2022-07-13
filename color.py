class Color:
    """A color.
    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.
    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """
    
    def __init__(self, color):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._COLORS = {"WHITE": [255, 255, 255, 255], "RED": [255, 0, 0, 255], "GREEN": [0, 255, 0, 255], "BLUE": [0, 0, 255, 255], "YELLOW": [255, 255, 0, 255], "INVISIBLE": [0, 0, 0, 0]}
        self._color_text = color
        self._color = self._COLORS[self._color_text]
        self._red = self._color[0]
        self._green = self._color[1]
        self._blue = self._color[2]
        self._alpha = 255

    def to_text(self):
        """
            Returns the text version of the Color object.
        """
        return self._color_text

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).
        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)