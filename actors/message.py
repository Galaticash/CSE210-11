from actors.actor import *

class Message(Actor):
    """
        An Actor that displays a given message at a given position.
    """
    def __init__(self, max_x, max_y, position, font_size, message, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        self._message = message
        self._x_pos = position[0]
        self._y_pos = position[1]
        self._position = Point(self._max_x, self._max_y, self._x_pos, self._y_pos)

    def get_display(self):
        """
            Returns the string that is used to display the Actor.
        """
        return self._message
