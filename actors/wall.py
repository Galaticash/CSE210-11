from actors.collision_actor import Collision_Actor, Hitbox, Point

class Wall(Collision_Actor):
    def __init__(self, max_x, max_y, top, bottom, left, right, size = 1, image="", color="WHITE"):
        super().__init__(max_x, max_y, size, image, color)
        self._position = Point(self._max_x, self._max_y, (right - left)//2, (bottom - top)//2)
        self._hitbox = Hitbox(top, bottom, left, right, 5)
