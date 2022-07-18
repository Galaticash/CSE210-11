from actors.collision_actor import Collision_Actor

# Obsolete class?
class Fighting_Actor(Collision_Actor):
    def __init__(self, name, position, width, height, image="blank.png", color="WHITE"):
        super().__init__(name, position, width, height, image, color)

        self._attack = 5