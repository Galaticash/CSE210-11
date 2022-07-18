from actors.enemy import Enemy
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

    def is_hit(self, other_collider):
        """
            The Boss is so big that he ignores the Top wall
        """
        if not (other_collider.get_name() == "TOP_WALL"):
            return super().is_hit(other_collider)
        else:
            return False