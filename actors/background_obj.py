
from actors.actor import Actor, Image
from actors.collision_actor import Collision_Actor

class background_obj(Actor):
    """
        An image displayed on the screen
    """
    def __init__(self, position, width, image="blank.png", rotation=0, scale=1, color="WHITE"):
        super().__init__(position, width, width, image, color)
        self._image = Image(image, scale, rotation)

    def get_display(self):
        return self._image

class collidable_obj(Collision_Actor):
    """
        A collidable image on the screen
    """
    def __init__(self, name, position, width, height, image="blank.png", rotation=0, scale=1, color="WHITE"):
        super().__init__(name, position, width, height, image, color)
        
        self._image = Image(image, scale, rotation)
        self._attack = 0

    # This actor will always be 'alive'
    def is_alive(self):
         return True

    # This actor doesn't move
    def move(self):
        pass

    # This actor doesn't recieve damage
    def damage(self, damage_points):
        pass

    # The actor will collide with other actors, but not recieve damage/update it's alive status
    def is_hit(self, other_collider):
        """
            If this object is hit, do nothing
        """
        if self._do_collisions and other_collider.get_name() == "Player":
            is_hit = self._hitbox.hit(other_collider.get_hitbox())
            if is_hit:
                pass
            return is_hit
        else:
            return False


# TO BE USED FOR LONG WALLS
class long_object(collidable_obj):
    def __init__(self, name, position, size, image="blank.png", rotation=0, scale=1, color="WHITE"):
        super().__init__(name, position, size, image, rotation, scale, color)
        width = size *3
        self._hitbox = self.calculate_hitbox(5, size, width)
