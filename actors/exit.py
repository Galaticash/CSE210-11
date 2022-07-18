from actors.collision_actor import Collision_Actor, Hitbox
from constants import DIRECTIONS

class Exit(Collision_Actor):
    def __init__(self, name, position, width, height, size = 1, image="blank.png", color="WHITE"):
    #def __init__(self, name, position, size, image="blank.png", color="WHITE"):
        super().__init__(name, position, width, height, image, color)
        padding = 5
        print(f"{self._name} wall created")
        self._hitbox = Hitbox(self._position, width, height, padding)
        # Hitbox(given_top, given_bottom, given_left, given_right, padding)

        limits = self._hitbox.get_limits()
        for direction in DIRECTIONS:
            print(f"   {direction} {limits[direction]}")

    def get_velocity(self):
        # wall does not have a velocity
        return [0, 0]

    def damage(self, damage_points):
        # Wall does not get damaged
        pass

    def move(self):
        # wall does not move
        pass