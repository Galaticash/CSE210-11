from actors.actor import *
from actors.hitbox import Hitbox

STEP_SIZE = 5
COLOR_TIMER_MAX = 2
COLLISION_TIMER = 50

class Collision_Actor(Actor):
    """
        An Actor that can collide with other Collision Actors.
    """
    def __init__(self, name, position, size, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        self._name = name

        # Health Points
        self._max_HP = 25
        self._current_HP = self._max_HP

        self._alive = True
        # Not all colliding Actors do damage to others.
        self._attack = 0

        self._color_timer = 0

        # If the Actor has control over their movement
        self._movement_control = True
        self._control_timer = 0
        self._control_reset = 0

        self._do_collisions = True
        self._collision_timer = 0
        self._collision_reset = COLLISION_TIMER

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
            *** UNIQUE IDENTIFIER ***
             Returns the unique name of the object
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

    def override_movement(self, time):
        """
            Overrides the Actor's movement control for a bit.
            NOTE: Time is NOT in seconds. It is the number of movement checks
            (Times that self.move is called)
        """
        self._movement_control = False
        self._control_timer = 0
        self._control_reset = time

    def override_update(self):
        """
            Checks if the Actor has regained control of their movement.
        """
        # Update the time until the user regains control
        self._control_timer += 1
        if self._control_timer >= self._control_reset:
            self._movement_control = True

    def move(self):
        """
            Moves based on its velocity. Also updates the Hitbox position.
        """
        # Checks if the _velocity has changed.
        self.get_velocity()

        # Slowly return velocity to normal from a sudden change
        # if self._velocity[0] > 1:
        #     self._velocity[0] -= 1
        # elif self._velocity[0] < -1:
        #     self._velocity[0] += 1
        # if self._velocity[1] > 1:
        #     self._velocity[1] -= 1
        # elif self._velocity[1] < -1:
        #     self._velocity[1] += 1

        dx = self._velocity[0] * self._step_size
        dy = self._velocity[1] * self._step_size

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
                    # Start timer of invulnerability
                    self._do_collisions = False
            else:
                # Color Timer instead of flashing Red for one second
                if self._color_timer >= COLOR_TIMER_MAX:
                    self._color_timer = 0
                    self._color = Color("WHITE")
            return is_hit
        else:
            # Not colliding with other actors, counter until it does
            if self._collision_timer >= self._collision_reset:
                self._collision_timer = 0
                self._do_collisions = True
            else:
                self._collision_timer += 1

            return False

    def is_alive(self):
        """
            Tells the scene manager if the Actor is alive still,
             otherwise it will be deleted. The Player, however 
             has a lives system, and will never have alive = False
        """
        return self._alive

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