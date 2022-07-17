from actors.collision_actor import Collision_Actor
from constants import GEM_ICON, BULLET_ICON, HEALTH_ICON, LIFE_ICON, KEY_ICON, BLANK_ICON

class Pickup(Collision_Actor):
    """
        An item that can be picked up (by the Player only)
    """
    def __init__(self, name, position, amount, size, color="WHITE"):        
        # Add a pickup identifier
        # VERY Hardcoded but it works

        name += "_p"
        if name[0] == "G":
            image = GEM_ICON
        elif name[0] == "B":
            image = BULLET_ICON
        elif name[0] == "H":
            image = HEALTH_ICON
        elif name[0] == "L":
            image = LIFE_ICON
        elif name[0] == "K":
            image = KEY_ICON
        else:
            image = BLANK_ICON

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

class ReusablePickup(Pickup):
    """
        A type of interactable that doesn't disappear after being 'picked up'
    """
    def __init__(self, name, position, amount, size, color="WHITE"):
        super().__init__(name, position, amount, size, color)

    def is_hit(self, other_collider):
        if self._do_collisions and other_collider.get_name() == "Player":
            is_hit = self._hitbox.hit(other_collider.get_hitbox())
            if is_hit:
                other_collider.pickup(self)
                # Just remove deletion
                #self._alive = False
            return is_hit
        else:
            return False