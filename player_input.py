import pyray

class Player_Input():
    """
        Determines if the user has pressed 
         a direction key (up, down, left, right)
         but only allows the Player to move in one
         direction at a time (up/down or left/right)
    """
    def __init__(self):
        self._dx = 0
        self._dy = 0
        
    def get_direction(self):
        """
            Changes the values of dx and dy and returns them.
            If X is changed, Y is reset, and vice versa.
            Moves in a grid-like pattern
            TODO: Implement an actual grid?
        """
        # The Left/Right directions
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
            self._dx = -1
            self._dy = 0
        elif pyray.is_key_down(pyray.KeyboardKey.KEY_D):
            self._dx = 1            
            self._dy = 0
        else:
            # The Up/Down directions
            if pyray.is_key_down(pyray.KeyboardKey.KEY_W):
                self._dy = -1
                self._dx = 0
            elif pyray.is_key_down(pyray.KeyboardKey.KEY_S):
                self._dy = 1
                self._dx = 0
            else:
                self._dy = 0
                self._dx = 0
        
        return [self._dx, self._dy]