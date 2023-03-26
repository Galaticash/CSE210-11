from actors.message import Message, Color, Point
from actors.hitbox import Hitbox
from constants import BUTTON_PADDING, BUTTON_COLOR, BUTTON_TEXT_COLOR, HARD_COLORS

class Button(Message):
    """
        A type of Message that returns if the cursor has been clicked in its Hitbox.
    """
    def __init__(self, position, height, message, image="", color=HARD_COLORS["WHITE"]):
        super().__init__(position, height, message, image, color)
        

        # Create a new hitbox using the width
        self._width = height * (len(self._message)//2)
        # Messages have their position on the top left corner
        self._center_position = Point(self._position.get_x() + self._width//2, self._position.get_y() + self._height//2 )
        self._hitbox = Hitbox(self._center_position, self._width, self._height, BUTTON_PADDING)

        self._text_color = Color(HARD_COLORS[BUTTON_TEXT_COLOR][0], HARD_COLORS[BUTTON_TEXT_COLOR][1], HARD_COLORS[BUTTON_TEXT_COLOR][2], HARD_COLORS[BUTTON_TEXT_COLOR][3])
        self._color = Color(HARD_COLORS[BUTTON_COLOR][0], HARD_COLORS[BUTTON_COLOR][1], HARD_COLORS[BUTTON_COLOR][2], HARD_COLORS[BUTTON_COLOR][3])

    def get_hitbox(self):
        """
            Returns the Button's hitbox (which is where it can be clicked).
        """
        return self._hitbox

    # TODO: Nonononono. Why is this in like 3 different places? Have like.. Image have a function like this (give pyray.Color, get tuple)
    def get_text_color(self):
        """
            Returns the Button's text color
        """
        return (self._text_color.r, self._text_color.g, self._text_color.b, self._text_color.a)

    def pressed(self, cursor_position):
        """
            Returns if the button hitbox has been pressed.
             (The cursor clicks inside the hitbox range)
        """
        return self._hitbox.clicked(cursor_position)