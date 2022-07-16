
from actors.actor import Actor, Image
from actors.collision_actor import Collision_Actor


class background_obj(Actor):
    """
        An image displayed on the screen
    """
    def __init__(self, position, size, image="blank.png", rotation=0, scale=1, color="WHITE"):
        super().__init__(position, size, image, color)
        self._image = Image(image, scale, rotation)

    def get_display(self):
        return self._image

class collidable_obj(Collision_Actor):
    """
        A collidable image on the screen
    """
    def __init__(self, name, position, size, image="blank.png", rotation=0, scale=1, color="WHITE"):
        super().__init__(name, position, size, image, color)
        self._image = Image(image, scale, rotation)

    def move(self):
        pass