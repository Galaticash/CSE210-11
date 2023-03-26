from actors.collision_actor import Collision_Actor, Hitbox, HARD_COLORS
from constants import DIRECTIONS

class Exit(Collision_Actor):
    def __init__(self, name, position, width, height, size = 1, image="blank.png", color=HARD_COLORS["WHITE"]):
    #def __init__(self, name, position, size, image="blank.png", color=HARD_COLORS["WHITE"]):
        super().__init__(name, position, width, height, image, color)
        padding = 5
        self._hitbox = Hitbox(self._position, width, height, padding)

    def get_velocity(self):
        # wall does not have a velocity
        return [0, 0]

    def damage(self, damage_points):
        # Wall does not get damaged
        pass

    def move(self):
        # wall does not move
        pass