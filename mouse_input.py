import pyray
from point import Point

class Mouse_Input():
    """
        Checks where the Mouse was clicked on the Window, 
         and returns a static Point position.
    """
    def click_position(self):
        """
            Checks if the user has clicked and returns the Point position of the cursor.
        """
    
        if pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
            # Return the position of the Mouse Cursor
            return Point(pyray.get_mouse_x(), pyray.get_mouse_y())
        return None