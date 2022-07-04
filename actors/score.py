from actors.message import Message
from color import Color

class Score(Message):
    """
        A type of Message that stores the Player's score.
    """
    def __init__(self, max_x, max_y, position, font_size, message, color="WHITE"):
        super().__init__(max_x, max_y, position, font_size, message, color)
        self._color = Color("WHITE")
        self._score = 0

    def add_points(self, points):
        """
            Adds points to the Player's Score.
        """
        self._score += points

    def get_score(self):
        """
            Returns the integer Score.
        """
        return self._score

    def get_display(self):
        """
            Returns the Score as a single string.
        """
        return f"{self._message} {self._score}"