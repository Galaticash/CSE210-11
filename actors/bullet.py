from actors.Fighting_Actor import Fighting_Actor

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
        self._scale = 100
        self._rotation = 275

        self._attack = 5

        self._velocity = velocity
        