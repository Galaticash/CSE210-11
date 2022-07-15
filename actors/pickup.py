from actors.collision_actor import Collision_Actor

GEM_ICON = "OtherSprites\\Diamond.png"
BULLET_ICON = "OtherSprites\\EnergyPack.png"
HEALTH_ICON = ""

class Pickup(Collision_Actor):
    """
        An item that can be picked up (by the Player only)
    """
    def __init__(self, name, position, amount, size, image="blank.png", color="WHITE"):        
        # Add a pickup identifier
        name += "_p"
        if name == "Gem_p":
            image = GEM_ICON
        elif name == "Bullet_p":
            image = BULLET_ICON
        elif name == "Heart_p":
            image = HEALTH_ICON

        super().__init__(name, position, size, image, color)

        self._amount = amount

    def get_amount(self):
        """
            Pickups can be multiple, get the amount to add to the Player's inventory.
        """        
        return self._amount

    def is_hit(self, other_collider):
        """
            The Player will pickup the item and add it to their inventory.
            The item is then deleted/removed.
            This object SHOULD NOT collide with other objects.. TODO fix that
        """
        if self._do_collisions and other_collider.get_name() == "Player":
            is_hit = self._hitbox.hit(other_collider.get_hitbox())
            if is_hit:
                other_collider.pickup(self)
                self._alive = False
            return is_hit
        else:
            return False