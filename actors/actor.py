from constants import Point
from color import Color
from actors.image import Image
import copy

class Actor():
    """
        An object that can be displayed on the GUI.
        Given the spawn position, the pxiel size, and color of itself. 
        Has a Point position on the screen
        Has a symbol to represent itself with, can be a single character or a string of them (Message).
        Has Getters for each Attribute so the GUI can properly display the Actor.
    """
    def __init__(self, position, width, height, image="blank.png", color = "WHITE"):
        # Spawn point at the center of the screen
        self._spawn_point = position
        self._position = self._spawn_point # Could replay the game and set the actor back to the start
        self._velocity = [0, 0] # The X and Y velocity
        self._velocity_prev = copy.copy(self._velocity) # Copy values only
        
        self._facing = [1, 0]
        self._alive = True

        self._symbol = "#" 
        self._image = image
        
        #self._size = size
        self._width = width
        # Assumes object is a square
        self._height = height

        self._base_color = Color(color)
        self._color = copy.copy(self._base_color)

    def revive(self):
        """
            Revives the Actor
        """
        self._alive = True

    def is_alive(self):
        """
            Tells the scene manager if the Actor is alive still,
             otherwise it will be deleted. The Player, however 
             has a lives system, and will never have alive = False
        """
        return self._alive

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
            Returns the string or image that is used to display the Actor.
        """
        # if self.
        return self._symbol

    def get_facing(self):
        """
            Returns the [x, y] direction the Actor is facing.
        """
        return self._facing

    def get_width(self):
        """
            Returns the width of the Actor.
        """
        return self._width

    def get_height(self):
        """
            Return the height of the Actor.
        """
        return self._height

    def get_size(self):
        """
            Returns the larger of the two values: width and height
        """
        return self._width if self._width > self._height else self._height

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