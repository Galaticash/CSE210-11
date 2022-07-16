from actors.actor import *
from actors.hitbox import Hitbox
from actors.image import Image
from constants import ACTOR_SIZE, FONT_SIZE
import copy

STEP_SIZE = 5
COLOR_TIMER_MAX = 2
COLLISION_TIMER = 75

# The frame at which the animation frame is updated
UPDATE_FRAME = 5

class Collision_Actor(Actor):
    """
        An Actor that can collide with other Collision Actors.
    """
    def __init__(self, name, position, size, image="blank.png", color="WHITE"):
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

        # For animation
        self._frame_counter = 0
        self._frames = [self._image]
        self._update_fame = UPDATE_FRAME
        self._current_frame = 0

        # Scale, rotation of image
        self._scale = 1
        self._facing = [1, 0]
        self._rotation = 0

        # How far the Actor moves per step
        self._step_size = STEP_SIZE

    def __eq__(self, other):
        """
            Can tell if it is the same instance if the name is the same.
        """
        return self._name == other._name
            

    def get_frame(self):
        """
            Animates the character, returns the current frame.
        """
        # If the Actor is standing still, stay on first frame (idle)
        # Also if the Actor only has one animation frame/sprite
        if self._velocity == [0, 0] or len(self._frames) == 1:
            return self._frames[0]

        # Check for the update frame
        self._frame_counter += 1
        if self._frame_counter == self._update_fame:
            # Reset the counter and update the animation frame,
            #  making sure to loop when it hits the end.
            self._frame_counter = 0
            self._current_frame += 1
            if self._current_frame == len(self._frames):
                self._current_frame = 1
        # Return the filepath of the current frame
        return self._frames[self._current_frame]

    def get_display(self):
        """
            Returns the frame of the Actor to display.
        """
        # Create and return an Image (the filepath, scale, rotation, and color/tint)
        texture = self.get_frame()        
        return Image(texture, self._scale, self._rotation, self._color)

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

    def get_attack(self):
        """
            Returns the damage this Actor does to other Fighting actors
        """
        return self._attack

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

    def get_velocity(self):
        """
            Returns the velocity, but also updates which way the actor is facing.
        """
        if not (self._velocity == [0, 0]):
            self._facing = self._velocity
        return super().get_velocity()

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

    def damage(self, damage_points):
        # If the Actor is already out of HP points
        if self._current_HP <= 0:
            # Should be dead
            self._alive = False
        else:
            # The Actor is damaged
            self._current_HP -= damage_points
            # If they are out of HP
            if self._current_HP <= 0:
                self._alive = False