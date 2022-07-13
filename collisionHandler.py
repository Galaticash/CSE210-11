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
                    print(f"Newton's law babey. {collider_one.get_name()} and {collider_two.get_name()}")
                    # Other collider hits the first collider back
                    collider_two.is_hit(collider_one)