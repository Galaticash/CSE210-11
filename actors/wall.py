from actors.collision_actor import Collision_Actor, Hitbox

class Wall(Collision_Actor):
    def __init__(self, name, position, given_top, given_bottom, given_left, given_right, size = 1, image="", color="WHITE"):
        super().__init__(name, position, size, image, color)
        self._hitbox = Hitbox(given_top, given_bottom, given_left, given_right, 5)
