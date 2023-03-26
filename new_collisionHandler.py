import copy
from constants import DIRECTIONS, FREEZE_TIME

# NOTE: Plan for redoing the collision system: Hitbox lines instead of rectangles
#       is_hit returns None, Top, Bottom, Left, Right
#       if second collider's the OPPOSITE direction, they are colliding (Top and Bottom touching, etc)
#       If they are a fighting object, fling away, oof ouch
#       If they are a normal collider, make sure they can't continue going the direction the other collider is

class collisionHandler():
    """
        An object that checks if 
    """
    def __init__(self):
        pass
        

    def stop_objects(self, collider_one, collider_two):
        """
        Given two colliders and the direction they are colliding, stops them from going through eachother.
        """
        # Stop them from continuing in the direction of the collision
        if collider_one.get_velocity() == self.reverse_velocity(collider_two.get_velocity()):
            print("Halt! You are violating the law.")
            collider_two.set_velocity([0, 0])
            collider_one.set_velocity([0, 0])

    def check_exit(self, player, exits):
        """
            Returns the direction the Player tries to exit.
        """
        for direction in DIRECTIONS:
            # If the wall has been hit by the Player
            if(exits[direction].is_hit(player)):
                return direction
        return None

    def reverse_velocity(self, velocity):
        """
            Reverses the direction of the collision.
        """
        return [velocity[0] * -1, velocity[1] * -1]

    def check_collisions(self, given_colliders):
        """
            Checks collisions between ALL Actors EXCEPT the Exits
        """
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
                    velocity_one = copy.copy(collider_one.get_velocity())
                    velocity_two = copy.copy(collider_two.get_velocity())
                    collision_direction = copy.copy(collider_one.get_velocity())
                    # Guarantee at least one collider is moving
                    # But if the first one isn't moving, get velocity from the second
                    if collision_direction == [0, 0]:                        
                        one_s_velocity = False
                        collision_direction = copy.copy(collider_two.get_velocity())
                        # Collider one is possibly a wall, pickup

                    elif velocity_one == self.reverse_velocity(velocity_two):
                        print("Head on collision! They ran right into eachother!")
                        # Fling