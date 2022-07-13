from actors.enemy import Enemy

class Boss(Enemy):
    def __init__(self, name, position, size, path="default", image="", color="WHITE"):
        super().__init__(name, position, size, path, image, color)
        self._max_HP = 40
        self._current_HP = self._max_HP

        self._attack = 5