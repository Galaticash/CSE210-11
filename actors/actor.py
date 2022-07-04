from color import Color
from point import Point
import copy

class Actor():
    """
        An object that can be displayed on the GUI.
        Given the maximum bounds of the screen, the font size, and color of itself. 
        Has a Point position on the screen
        Has a symbol to represent itself with, can be a single character or a string of them (Message).
        Has Getters for each Attribute so the GUI can properly display the Actor.
    """
    def __init__(self, max_x, max_y, font_size, color = "WHITE"):
        self._max_x = max_x
        self._max_y = max_y
        # TODO: some calculations for spawn point
        self._spawn_point = Point(max_x, max_y, max_x//2, max_y//2)
        self._position = self._spawn_point # Could replay the game and set the actor back to the start
        self._velocity = [0, 0] # The X and Y velocity
        self._velocity_prev = copy.copy(self._velocity) # Copy values only
        self._symbol = "#"
        self._font_size = font_size
        self._base_color = Color(color)
        self._color = copy.copy(self._base_color)

    def move(self, x, y):
        """
            Moves the Actor to a specified x/y coordinate.
        """
        self._position.set_position(x, y)
    
    def get_point_position(self):
        """
            Returns the Point position of the Actor.
        """
        return self._position

    def get_x(self):
        """
            Returns the X position of the Actor.
        """
        return self._position.get_x()

    def get_y(self):
        """
            Returns the Y position of the Actor.
        """
        return self._position.get_y()

    def set_velocity(self, new_velocity):
        """
            Given a velocity [x, y], changes the Actor's velocity.
        """
        self._velocity_prev = self._velocity[:]
        self._velocity = new_velocity

    def get_velocity(self):
        """
            Gets the current dx/dy of the Actor as [dx, dy].
        """
        return self._velocity
 
    def get_previous_velocity(self):
        """
            Returns the previous velocity of the Actor.
        """
        return self._velocity_prev

    def get_display(self):
        """
            Returns the character or string that is used to display the Actor.
        """
        return self._symbol

    def get_font_size(self):
        """
            Returns the font size of the Actor.
        """
        return self._font_size

    def set_color(self, color):
        """
            Sets the color of the Actor.
        """        
        self._color = Color(color)

    def reset_color(self):
        """
            Resets the color of the Actor, from turning red when hit.
        """
        self._color = copy.copy(self._base_color)

    def get_color(self):
        """
            Returns the tuple Color of the Actor.
        """
        return self._color.to_tuple()