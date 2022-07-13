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
        #for wall_pos in DIRECTIONS:
        # DEBUG: Testing collisions with Top hitbox
        # print("\tPlayer vs TOP")
        if player.get_hitbox().hit(given_walls["TOP"].get_hitbox()):
            print(f"Attempting to exit via TOP")
            return "TOP"
        return None

    def check(self, given_colliders):
        """
            Checks if there has been a collision between any of the colliders
        """
        # TODO: Is there a way to more efficiently check collisions, check only close ones? Check each one against each other collider (VERY inefficient)?
        # TODO: More effectivley handle color reset, only reset the color if /was/ hit but currently not hit
        
        # NOTE: The last collider is colliding with itself

        # A more generalized Collision Handler
        colliders_one = given_colliders.copy()
        colliders_two = given_colliders.copy()[1:]

        for collider_one in colliders_one:
            # Check every collider in list one against those in list two, 
            # removing items from two if they are the same (no comparison needed)
            for collider_two in colliders_two:
                # Don't check the same collider against itself
                if collider_one == collider_two:
                    colliders_two.pop(colliders_two.index(collider_two))
                else:
                    colliders = [collider_one, collider_two]
                    # Check if there is a collision between the two colliders
                    if collider_one.is_hit( collider_two.get_hitbox()):
                        # Indicate there has been a collision.
                        # Play a sound?
                        # print(f"{collider_one} and {collider_two} have collided!")
                        collider_one.damage(collider_two.get_attack())
                        collider_one.set_color("RED")
                        collider_two.damage(collider_one.get_attack())
                        collider_two.set_color("RED")
                    else:
                        for collider in colliders:
                            # There has been no collision, do nothing
                            # Only reset color for those with was_hit == True?
                            collider.reset_color()