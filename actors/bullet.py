from actors.Fighting_Actor import Fighting_Actor
from constants import ROTATION

IMAGE_SOURCE = "Bolt\\"
IMAGE_NAME = "arrow1_"
IMAGE_RANGE = [6, 11]
IMAGE_FILETYPE = ".png"

class Bullet(Fighting_Actor):
    """
        A Bullet fired from the Player to do damage
    """
    def __init__(self, name, position, velocity, size, image="Bolt\\arrow1_6.png", color="WHITE"):
        super().__init__(name, position, size, image, color)
        # Has no Health Points so it can be immediately destroyed on impact
        self._max_HP = 0
        self._current_HP = 0

        self._frames = ["Bolt\\arrow1_6.png", "Bolt\\arrow1_7.png", "Bolt\\arrow1_8.png", "Bolt\\arrow1_9.png", "Bolt\\arrow1_10.png", "Bolt\\arrow1_11.png"]
        self._scale = 2

        self._rotation = self.find_rotation(velocity)

        self._attack = 5

        self._velocity = velocity
        
    def find_rotation(self, velocity):
        """
            Find the proper rotation of the Bullet (limited to 90 degree intervals)
        """
        rotation = ROTATION[0]
        if velocity == [0, 0]:
            return rotation

        # If velocity_x is nothing, check y
        if velocity[0] == 0:
            if velocity[1] > 0:
                rotation = ROTATION[0]
            else:
                rotation = ROTATION[2]
        # Velocity Y has to be nothing (grid-based)
        else:
            if velocity[0] > 0:
                rotation = ROTATION[3]
            else:
                rotation = ROTATION[1]
        
        return rotation

    def is_hit(self, other_collider):
        """
            The bullet is deleted if it hits anything.
        """
        hit_something = super().is_hit(other_collider)
        if hit_something:
            # print(f"Bullet hit {other_collider.get_name()}")
            self._alive = False

        return hit_something