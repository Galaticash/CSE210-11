import copy
DIRECTIONS = ["TOP", "BOTTOM", "LEFT", "RIGHT"]

# TODO: Objects cannot move through eachother
# TODO: Check collisions between each object, only once and efficiently

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

    def check(self, given_colliders):
        """
            Checks if there has been a collision between any of the colliders
        """
        # TODO: Is there a way to more efficiently check collisions, check only close ones? 
        # But I guess I'll have to check each one against each other collider (not too efficient, but effective)
        
        # This is the same way I coded it (I know bc there are the same bugs), 
        #  but it just looks a little neater
        # For every item in the list (while also counting with i)
        for i, collider_one in enumerate(given_colliders):
            # Check a sub section of the list
            for j in range(i + 1, len(given_colliders)):
                collider_two = given_colliders[j]
                # Check if the first object collided with the other object
                if collider_one.is_hit(collider_two):
                    # print(f"{collider_one.get_name()} and {collider_two.get_name()}")
                    # Other collider hits the first collider back
                    collider_two.is_hit(collider_one)

                    # Find collision direction, send colliders in opposite directions?
                    # So even if the Player isn't moving, sees that the other actor was coming in from the left and sends the Player flying to the left?

                    # Need a way to not collide more than once
                    # Option 1: Change Velocity
                    collision_direction = copy.copy(collider_one.get_velocity())
                    if collision_direction == [0, 0]:
                        collision_direction = copy.copy(collider_two.get_velocity())
                        collider_one.set_velocity(collision_direction)
                        opposite_velocity = [collision_direction[0]* -1, collision_direction[1]* -1]
                        collider_two.set_velocity(opposite_velocity)
                    else:
                        collider_two.set_velocity(collision_direction)
                        opposite_velocity = [collision_direction[0]* -1, collision_direction[1]* -1]
                        collider_one.set_velocity(opposite_velocity)

                    # Option 1 Part 2: Add some kick to the velocity, Knockback


                    # Option 3: Timer - can only check for collisions every # frames/checks
                    # Kinda implemented? Would be handled in collision actor