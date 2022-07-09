from actors.actor import *
from actors.hitbox import Hitbox

STEP_SIZE = 5

class Collision_Actor(Actor):
    """
        An Actor that can collide with other Collision Actors.
    """
    def __init__(self, max_x, max_y, size, image="", color="WHITE"):
        super().__init__(max_x, max_y, size, image, color)
        self._hitbox = Hitbox(len(self._symbol), self._size)
        # How many pixels the Actor travels per Move method call.
        self._step_size = STEP_SIZE

    def update_hitbox(self):
        """
            Re-calculate the edges of the hitbox.
        """
        self._hitbox.update(self._position)

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

        # Update the Actor's position
        self._position.add_velocity(self._velocity[0]  * self._step_size, self._velocity[1]  * self._step_size)
        
        # Update the hitbox's position.
        self.update_hitbox()

    def is_hit(self, other_collider):
        """
            Check if the Point position of the other 
             collider is within the Hitbox of this actor.
        """
        return self._hitbox.is_hit(other_collider.get_point_position())
