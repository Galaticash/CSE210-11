from actors.collision_actor import Collision_Actor
from constants import PICKUP_SIZE, BOSS_KEY_NAME, GEM_ICON, BULLET_ICON, HEALTH_ICON, LIFE_ICON, KEY_ICON, BLANK_ICON, BULLET_NAME, GEM_NAME, HEALTH_NAME, LIFE_NAME

class Pickup(Collision_Actor):
    """
        An item that can be picked up (by the Player only)
    """    
    def __init__(self, name, position, amount, width = PICKUP_SIZE, color="WHITE"):        
        # Add a pickup identifier, VERY Hardcoded but it works
        # Name without the number (0 - 9)
        if name[0:-1] == BOSS_KEY_NAME:
            image = KEY_ICON
        elif name[0:-1] == GEM_NAME:
            image = GEM_ICON
        elif name[0:-1] == BULLET_NAME:
            image = BULLET_ICON
        elif name[0:-1] == HEALTH_NAME:
            image = HEALTH_ICON
        elif name[0:-1] == LIFE_NAME:
            image = LIFE_ICON
        else:
            image = BLANK_ICON
        
        # Pickup identifier (if obj.get_name()[-2] == "_p")
        name += "_p"

        super().__init__(name, position, width, width, image, color)

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
    def __init__(self, name, position, amount, width = PICKUP_SIZE, color="WHITE"):
        super().__init__(name, position, amount, width, color)

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