from collision_actor import Collision_Actor

class Fighting_Actor(Collision_Actor):
    def __init__(self, max_x, max_y, size, image="", color="WHITE"):
        super().__init__(max_x, max_y, size, image, color)
        self._max_HP = 10
        self._current_HP = 10
        
        # Player will do damage with a weapon (for Player -> 0, but their weapon)
        self._collision_damage = 1
