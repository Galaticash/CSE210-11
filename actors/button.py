from actors.message import Message, Color
from actors.hitbox import Hitbox

class Button(Message):
    
    """
        A type of Message that returns if the cursor has been clicked in its Hitbox.
    """
    def __init__(self, max_x, max_y, position, size, message, image="", color="WHITE"):
        super().__init__(max_x, max_y, position, size, message, image, color)
        self._hitbox = Hitbox(len(self._message)//2, self._size, 15)
        self._hitbox.update(self._position)
        self._color = Color("GREEN")

    def get_hitbox(self):
        """
            Returns the Button's hitbox (which is where it can be clicked).
        """
        return self._hitbox

    def pressed(self, cursor_position):
        """
            Returns if the button hitbox has been pressed.
             (The cursor clicks inside the hitbox range)
        """
        return self._hitbox.is_hit(cursor_position)