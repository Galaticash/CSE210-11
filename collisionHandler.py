class Collision_Handler():
    """
        Handles the Collisions of the game, given a Cast of Colliding Actors.
    """
    def __init__(self):
        pass
    
    def check(self, given_colliders):
        """
            Checks if there has been a collision between any of the colliders
        """
        # TODO: Is there a way to more efficiently check collisions, check only close ones? Check each one against each other collider (VERY inefficient)?
        # TODO: More effectivley handle color reset, only reset the color if /was/ hit but currently not hit
        
        # A more generalized Collision Handler
        colliders_one = given_colliders.copy()
        colliders_two = given_colliders.copy()[1: -1]
        for collider_one in colliders_one:
            # Check every collider in list one against those in list two, 
            # removing items from two if they are the same (no comparison needed)
            for collider_two in colliders_two:
                if collider_one == colliders_two:
                    colliders_two.pop(collider_two)
                else:
                    colliders = [collider_one, collider_two]
                if collider_one.is_hit(collider_two):
                    # Indicate there has been a collision.
                    # Play a sound?
                    for collider in colliders:
                        collider.set_color("RED")
                else:
                    for collider in colliders:
                        # There has been no collision, do nothing
                        # Only reset color for those with was_hit == True?
                        collider.reset_color()