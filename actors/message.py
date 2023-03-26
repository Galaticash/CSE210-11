from actors.actor import *

class Message(Actor):
    """
        An Actor that displays a given message at a given position.
    """
    def __init__(self, position, height, message, image="", color=HARD_COLORS["WHITE"]):
        super().__init__(position, height, height, image, color)
        self._message = message
        self._x_pos = position.get_x()
        self._y_pos = position.get_y()

    def get_size(self):
        """
            Returns how tall the letters are to be printed.
        """
        return self._height

    def get_display(self):
        """
            Returns the string that is used to display the Actor.
        """
        return self._message

class Temp_Message(Message):
    """
        A type of message that fades over time
    """
    def __init__(self, position, height, message, fade_speed, image="", color=HARD_COLORS["WHITE"]):
        super().__init__(position, height, message, image, color)
        self._fade_speed = fade_speed
        self._timer = 0
       
    def is_alive(self):
        return super().is_alive()

    def get_color(self):
        # Make a faded version of the color
        color = [self._color.r, self._color.g, self._color.b, self._color.a]
        # self._color.to_tuple()

        transparency = 255 - self._timer
        if self._timer < 255:
            self._timer += self._fade_speed
        else:
            transparency = 0
            self.is_alive = False
            
        fading = (color[0], color[1], color[2], transparency)
         
        return fading

