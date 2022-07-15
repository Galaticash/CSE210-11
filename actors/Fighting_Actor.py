from actors.collision_actor import Collision_Actor

# Obsolete class?
class Fighting_Actor(Collision_Actor):
    def __init__(self, name, position, size, image="blank.png", color="WHITE"):
        super().__init__(name, position, size, image, color)

        self._attack = 5