from actors.actor import *
from actors.hitbox import Hitbox

STEP_SIZE = 5
COLOR_TIMER_MAX = 20

class Collision_Actor(Actor):
    """
        An Actor that can collide with other Collision Actors.
    """
    def __init__(self, name, position, size, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        self._name = name
        self._do_collisions = True

        self._alive = True
        # Not all colliding Actors do damage to others.
        self._attack = 0

        self._color_timer = 0

        # Hitbox math
        top = (self._position.get_y() - self._size//2)
        bottom = (self._position.get_y() + self._size//2) 
        left = (self._position.get_x() - (self._size//2)) 
        right = (self._position.get_x() + (self._size//2)) 
        self._hitbox = Hitbox(top, bottom, left, right, -20)

        # How far the Actor moves per step
        self._step_size = STEP_SIZE

    def __eq__(self, other):
        """
            Can tell if it is the same instance if the name is the
        """
        return self._name == other._name
            
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

    def get_name(self):
        """
            TEMPORARY: Returns the unique name of the object
             Names are being used to determine if compared
             colliding actors are the same instance.
        """
        return self._name

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
             collider is within the Hitbox of this actor,
             but only when doing collisions
        """
        if self._do_collisions:
            is_hit = self._hitbox.hit(other_collider.get_hitbox())
            # Only every 10 or so checks will the color change back to normal?
            self._color_timer += 1
            if is_hit:
                other_damage = other_collider.get_attack()
                if other_damage > 0:
                    self.damage(other_damage)
                    self._color = Color("RED")
            else:
                if self._color_timer >= COLOR_TIMER_MAX:
                    self._color_timer = 0
                    self._color = Color("WHITE")
            return is_hit
        else:
            # Not colliding with other actors, stay normal color
            self._color = Color("WHITE")
            return False

    def get_attack(self):
        """
            Returns the damage this Actor does to other Fighting actors
        """
        return self._attack

    def damage(self, damage_points):
        # If the Actor is already out of HP points
        if self._current_HP <= 0:
            # Don't do anything
            pass
        else:
            # The Actor is damaged
            self._current_HP -= damage_points
            # If they are out of HP
            if self._current_HP <= 0:
                pass
               #self._alive = False