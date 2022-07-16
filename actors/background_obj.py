
from actors.actor import Actor
from actors.collision_actor import Collision_Actor


class background_obj(Actor):
    def __init__(self, position, size, image="blank.png", color="WHITE"):
        super().__init__(position, size, image, color)
    



class collidable_obj(Collision_Actor):
    def __init__(self, name, position, size, image="blank.png", color="WHITE"):
        super().__init__(name, position, size, image, color)

    
    
