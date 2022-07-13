from actors.actor import *

class Message(Actor):
    
    """
        An Actor that displays a given message at a given position.
    """
    def __init__(self, position, size, message, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        self._message = message
        self._x_pos = position.get_x()
        self._y_pos = position.get_y()

    def get_display(self):
        """
            Returns the string that is used to display the Actor.
        """
        return self._message
