from actors.Fighting_Actor import Fighting_Actor

#BULLET_IMAGE = 

class Bullet(Fighting_Actor):
    """
        A Bullet fired from the Player to do damage
    """
    def __init__(self, name, position, velocity, size, image="", color="WHITE"):
        super().__init__(name, position, size, image, color)
        # Has no Health Points so it can be immediately destroyed on impact
        self._max_HP = 0
        self._current_HP = 0

        self._attack = 5

        self._velocity = velocity
        