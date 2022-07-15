from actors.message import Message, Color
from actors.hitbox import Hitbox

BUTTON_PADDING = 5
BUTTON_COLOR = "GREEN"
BUTTON_TEXT_COLOR = "WHITE"

class Button(Message):
    """
        A type of Message that returns if the cursor has been clicked in its Hitbox.
    """
    def __init__(self, position, size, message, image="", color="WHITE"):
        super().__init__(position, size, message, image, color)

        # Hitbox math
        # POSITION IS TOP LEFT
        top = (self._position.get_y())
        bottom = (self._position.get_y() + self._size) 
        left = (self._position.get_x()) 
        right = (self._position.get_x() + (self._size//2 * len(self._message))) 
        self._hitbox = Hitbox(top, bottom, left, right, BUTTON_PADDING)

        self._text_color = Color(BUTTON_TEXT_COLOR)
        self._color = Color(BUTTON_COLOR)

    def get_hitbox(self):
        """
            Returns the Button's hitbox (which is where it can be clicked).
        """
        return self._hitbox

    def get_text_color(self):
        """
            Returns the Button's text color
        """
        return self._text_color.to_tuple()

    def pressed(self, cursor_position):
        """
            Returns if the button hitbox has been pressed.
             (The cursor clicks inside the hitbox range)
        """
        return self._hitbox.clicked(cursor_position)