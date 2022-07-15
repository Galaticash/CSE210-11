from actors.collision_actor import Collision_Actor, Hitbox

class Wall(Collision_Actor):
    def __init__(self, name, position, given_top, given_bottom, given_left, given_right, size = 1, image="blank.png", color="WHITE"):
        super().__init__(name, position, size, image, color)
        padding = 5
        self._hitbox = Hitbox(given_top, given_bottom, given_left, given_right, padding)

    def get_velocity(self):
        # wall does not have a velocity
        return [0, 0]

    def damage(self, damage_points):
        # Wall does not get damaged
        pass

    def move(self):
        # wall does not move
        pass