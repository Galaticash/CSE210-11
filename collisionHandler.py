import copy
from constants import DIRECTIONS, FREEZE_TIME, PLAYER_NAME

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

    def fling_object(self, collider):
        # Fling only one object in the opposite direction it was travelling
        opposite_velocity = self.reverse_velocity(collider.get_velocity())
        self.freeze_movement(collider)
        collider.set_velocity(opposite_velocity)

    def fling_objects(self, collision_direction, collider_one, collider_two):
        """
            Given two colliders and the direction they are colliding, flings them opposite directions.
        """
        # Freezes the collider's ability to change their velocity
        #   until after they have been flung.
        self.freeze_movement(collider_one)
        self.freeze_movement(collider_two)
        
        # Send them flying opposite directions
        collider_two.set_velocity(collision_direction)
        opposite_velocity = self.reverse_velocity(collision_direction)
        collider_one.set_velocity(opposite_velocity)

    def reverse_velocity(self, velocity):
        """
            Reverses the direction of the collision.
        """
        return [velocity[0] * -1, velocity[1] * -1]

    def stop_object(self, collision_direction, collider):
        # stop the object from moving in the collision direction
        if collider.get_velocity() == collision_direction:
            collider.set_velocity([0, 0])

    def freeze_movement(self, collider):
        """
            Freezes the movement of the given collider
        """
        # Freeze the collider's ability to move
        collider.override_movement(FREEZE_TIME)

    def check_exit(self, given_colliders):
        """
            Checks if there has been a collision between any of the colliders
        """
        # TODO: Is there a way to more efficiently check collisions, check only close ones? 
        # But I guess I'll have to check each one against each other collider (not too efficient, but effective)

        # Will check if the Player is exiting
        exit_direction = None

        # For every item in the list (while also counting with i)
        for i, collider_one in enumerate(given_colliders):
            # Check a sub section of the list
            for j in range(i + 1, len(given_colliders)):
                collider_two = given_colliders[j]
                # Check if the colliders have hit eachother
                # BOTH have to return True, since some Actors ignore collisions
                if collider_one.is_hit(collider_two) and collider_two.is_hit(collider_one):
                    # Will reverse the direction the objects are currently travelling
                    one_s_velocity = True
                    collision_direction = copy.copy(collider_one.get_velocity())

                    # Guarantee at least one collider is moving
                    # But if the first one isn't moving, get velocity from the second
                    if collision_direction == [0, 0]:                        
                        one_s_velocity = False
                        collision_direction = copy.copy(collider_two.get_velocity())
                    
                    # Do not fling the colliders if one is a Pickup OR an Exit
                    if collider_one.get_name()[-2:] == "_p" or collider_two.get_name()[-2:] == "_p":
                        pass
                    # If one collider is the Player and the other is an Exit
                    elif (collider_one.get_name() == PLAYER_NAME or collider_two.get_name() == PLAYER_NAME):
                        if (collider_one.get_name() in DIRECTIONS):
                            exit_direction = collider_one.get_name()
                        elif(collider_two.get_name() in DIRECTIONS):
                            exit_direction = collider_two.get_name()
                        else:
                            # The Player is colliding with something else
                            self.fling_objects(collision_direction, collider_one, collider_two)
    
                        if exit_direction == None:
                            self.fling_objects(collision_direction, collider_one, collider_two)
                            # Normal collisions - stop movement in collision direction
                        else:
                            pass

                    else:                    
                        self.fling_objects(collision_direction, collider_one, collider_two)

        return exit_direction