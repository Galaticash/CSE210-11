class Point:
    """A distance from a relative origin (0, 0).
    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.
    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y
        #[x, y]

    # Called when point1 == point2?
    def __eq__(self, other):
        if self._x == other._x:
            if self._y == other._y:
                return True
        # Either the x or y position don't match
        return False

    def set_position(self, x, y):
        """
            Changes the x and y position of the point.
        """
        self._x = x
        self._y = y

    def get_x(self):
        """
            Gets the horizontal distance.
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """
            Gets the vertical distance.
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def add_velocity(self, dx, dy):
        """
            Changes the x and y position based off of the velocity 
            (aka change in position)
        """
        self._x += dx
        self._y += dy