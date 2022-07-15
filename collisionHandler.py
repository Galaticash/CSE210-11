import copy
from point import Point
from constants import DIRECTIONS
from actors.pickup import Pickup

FREEZE_TIME = 50

# TODO: Objects should not move through eachother
# TODO: Objects get stuck in an infinite loop of colliding, esp when pushed by another object
#       This is the objects colliding in the rectange instead of borders? so cut out a square
#    in the middle where it says, hold up, you're in the middle of an object instead of on the edge?

class Collision_Handler():
    """
        Handles the Collisions of the game, given a Cast of Colliding Actors.
    """
    def __init__(self):
        pass
    
    def check_exit(self, player, given_walls):
        """
            Checks if the Player is exiting, returns which way they are leaving.
        """
        for wall_pos in DIRECTIONS:
            if player.get_hitbox().hit(given_walls[wall_pos].get_hitbox()):
                print(f"Attempting to exit via {wall_pos}")
                return wall_pos
        return None

    def fling_objects(self, collision_direction, collider_one, collider_two):
        self.freeze_movement(collider_one, collider_two)
        # Send them flying opposite directions

        collider_two.set_velocity(collision_direction)
        opposite_velocity = [collision_direction[0]* -1, collision_direction[1]* -1]
        collider_one.set_velocity(opposite_velocity)

    def freeze_movement(self, collider_one, collider_two):
        # Freeze the collider's ability to move
        collider_one.override_movement(FREEZE_TIME)
        collider_two.override_movement(FREEZE_TIME)

    def check(self, given_colliders):
        """
            Checks if there has been a collision between any of the colliders
        """
        # TODO: Is there a way to more efficiently check collisions, check only close ones? 
        # But I guess I'll have to check each one against each other collider (not too efficient, but effective)

        # For every item in the list (while also counting with i)
        for i, collider_one in enumerate(given_colliders):
            # Check a sub section of the list
            for j in range(i + 1, len(given_colliders)):
                collider_two = given_colliders[j]
                # Check if the first object collided with the other object
                if collider_one.is_hit(collider_two):
                    # Other collider hits the first collider back
                    collider_two.is_hit(collider_one)

                    # Will reverse the direction the objects are currently travelling
                    collision_direction = copy.copy(collider_one.get_velocity())
                    
                    # Guarantee at least one collider is moving
                    # But if the first one isn't moving, get velocity from the second
                    if collision_direction == [0, 0]:
                        collision_direction = copy.copy(collider_two.get_velocity())
                    
                    # Do not fling the colliders if one is a pickup OR a wall
                    if isinstance(collider_one, Pickup) or isinstance(collider_two, Pickup):
                        pass
                    elif collider_one.get_name() in DIRECTIONS:
                        pass
                    else:
                        self.fling_objects(collision_direction, collider_one, collider_two)
