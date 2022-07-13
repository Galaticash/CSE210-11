from actors.collision_actor import Collision_Actor, Hitbox, Point

class Wall(Collision_Actor):
    def __init__(self, position, top, bottom, left, right, size = 1, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        self._hitbox = Hitbox(top, bottom, left, right, 5)
