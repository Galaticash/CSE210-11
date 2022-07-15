from actors.collision_actor import Collision_Actor
from actors.image import Image
# TODO: Fix Collision Actor to have image settings

BULLET_ICON = ""
GEM_ICON = "OtherSprites\\Diamond.png"

class Pickup(Collision_Actor):
    def __init__(self, name, position, amount, size, image="", color="WHITE"):        
        # Add a pickup identifier
        name += "_p"
        super().__init__(name, position, size, image, color)
        if name == "Gem_p":
            self._frames = GEM_ICON
        elif name == "Bullet_p":
            self._frames = GEM_ICON
        else:
            self._frames = GEM_ICON
        self._texture = self._frames

        self._scale = 1
        self._rotation = 0
        
        self._amount = amount

    def get_display(self):
        return Image(self._texture, self._scale, self._rotation, self._color)

    def get_amount(self):        
        return self._amount

    def is_hit(self, other_collider):
        if other_collider.get_name == "Player" and self._do_collisions:
            is_hit = self._hitbox.hit(other_collider.get_hitbox())
            if is_hit:
                other_collider.pickup(self)
                self._alive = False