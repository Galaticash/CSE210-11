from actors.actor import *
from actors.hitbox import Hitbox

STEP_SIZE = 5

class Collision_Actor(Actor):
    """
        An Actor that can collide with other Collision Actors.
    """
    def __init__(self, position, size, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        top = (self._position.get_y() - self._size//2)
        bottom = (self._position.get_y() + self._size//2) 
        left = (self._position.get_x() - (self._size//2)) 
        right = (self._position.get_x() + (self._size//2)) 
        self._hitbox = Hitbox(top, bottom, left, right)

    # def _set_limits(self):
    #     # The position is at the Top Left (determined by python.draw_text/etc)
    #     self._limits[DIRECTIONS[0]] = (self._position.get_y() - self._size//2) - self._padding
    #     self._limits[DIRECTIONS[2]] = (self._position.get_x() - (self._size//2)) - self._padding

    #     # Top point + (down) font_size = Bottom point
    #     self._limits[DIRECTIONS[1]] = (self._position.get_y() + self._size//2) + self._padding

    #     # Left point + (right) font_size * width = Right point
    #     # The right side of the hitbox must be adjusted to the length of the symbol
    #     self._limits[DIRECTIONS[3]] = (self._position.get_x() + (self._size//2)) + self._padding

        # How many pixels the Actor travels per Move method call.
        self._step_size = STEP_SIZE

    def get_hitbox(self):
        """
            Returns the hitbox object.
        """
        return self._hitbox

    def get_display(self):
        """
            Returns the Image of the Actor
        """
        return self._image

    def move(self):
        """
            Moves based on its velocity. Also updates the Hitbox position.
        """
        # Checks if the _velocity has changed.
        self.get_velocity()

        dx = self._velocity[0]  * self._step_size
        dy = self._velocity[1]  * self._step_size

        # Update the Actor's position
        self._position.add_velocity(dx, dy)
        
        # Update the hitbox's position.
        #self._hitbox.add_velocity(dx, dy)
        self._hitbox.update_position(self._position, self._size)

    def is_hit(self, other_collider):
        """
            Check if the Point position of the other 
             collider is within the Hitbox of this actor.
        """
        return self._hitbox.hit(other_collider)
