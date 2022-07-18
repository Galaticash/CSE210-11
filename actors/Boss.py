from actors.enemy import Enemy
from actors.hitbox import Hitbox
from constants import BOSS_HP, BOSS_ATTACK

class Boss(Enemy):
    """
        A type of Enemy that is bigger and badder than a normal minion.
    """
    def __init__(self, name, position, width, height, path, image="blank.png", color="WHITE"):
        super().__init__(name, position, width, height, path, image, color)
        self._max_HP = BOSS_HP
        self._current_HP = self._max_HP

        self._attack = BOSS_ATTACK