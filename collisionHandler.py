class Collision_Handler():
    """
        Handles the Collisions of the game, given a Cast of Colliding Actors.
    """
    def __init__(self, cast):
        self._cast = cast
        # Gets only the Players/Colliders.
        self._players = self._cast.get_players()
    
    def update_colliders(self):
        """
            Double checks if the Cast has added new Players/Colliders.
        """
        self._colliders = self._cast.get_players()

    def check(self):
        """
            Checks if there has been a collision between the two Players.
        """
        self.update_colliders()
        
        # TODO: More dynamically check collisions, check only close ones? Check each one against each other collider (VERY inefficient)?
        # TODO: Different return values to tell Director which Collider won/lost --> currently handled only within Collision Handler
        
        # A more generalized Collision Handler
        # # TODO: More effectivley handle color reset, only reset the color if /was/ hit but currently not hit
        #   colliders_one = self._colliders
        #   colliders_two = self._colliders [1: -1]
        # for collider_one in colliders_one:
        #     # Check every collider in list one against those in list two, 
        #     # removing items from two if they are the same (no comparison needed)
        #     for collider_two in colliders_two:
        #         #if collider_one == colliders_two:
        #         #    colliders_two.pop(collider_two)
        #         #else:
        #         colliders = [collider_one, collider_two]
        #         if collider_one.is_hit(collider_two):
        #             # Indicate there has been a collision.
        #             for collider in colliders:
        #                 collider.set_color("RED")
        #             return True
        #         else:
        #             for collider in colliders:
        #               # Check for only those with was_hit == True?
        #                 collider.reset_color()
        #             return False