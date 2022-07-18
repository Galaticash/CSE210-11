DIRECTIONS = ["TOP", "BOTTOM", "LEFT", "RIGHT"]

class Hitbox():
    """
        A 2D Hitbox that determines if a Point position is within it's bounds.
    """    
    #def __init__(self, top, bottom, left, right, padding = 0):
    def __init__(self, position, width, height, padding = 0):
        # NEW: Hitbox(position, width, height, padding)
        self._position = position
        self._height = height
        self._width = width
        self._padding = padding
        
        # The bounds of the Hitbox
        self._limits = self.calculate_limits()
        
        # print(f"Box created c: {self._limits['LEFT']} to {self._limits['RIGHT']} | y: {self._limits['TOP']} to {self._limits['BOTTOM']}.")
        self._is_hit = False

    def calculate_limits(self):
        # Hitbox math
        top = (self._position.get_y() - self._height//2)
        bottom = (self._position.get_y() + self._height//2)
         
        left = (self._position.get_x() - (self._width//2))
        right = (self._position.get_x() + (self._width//2))

        return {"TOP": top - self._padding, "BOTTOM": bottom + self._padding, "LEFT": left - self._padding, "RIGHT": right + self._padding}

    def get_limits(self):
        return self._limits

    def overrite_position(self, new_pos):
        self._position = new_pos
        self._limits = self.calculate_limits()

    def update_position(self, dx, dy):
        self.add_velocity(dx, dy)

    # def update_position(self, position, size):
    #     """
    #         Updates the Actor's Hitbox according to the Actor's position.
    #     """
    #      # The position is at the Top Left (determined by python.draw_text/etc)
    #     self._limits[DIRECTIONS[0]] = position.get_y() - size//2  - self._padding
    #     self._limits[DIRECTIONS[2]] = position.get_x() - size//2  - self._padding

    #     # Top point + (down) font_size = Bottom point
    #     self._limits[DIRECTIONS[1]] = (position.get_y() + size//2) + self._padding

    #     # Left point + (right) font_size * width = Right point
    #     # The right side of the hitbox must be adjusted to the length of the symbol
    #     self._limits[DIRECTIONS[3]] = (position.get_x() + size//2) + self._padding

    def add_velocity(self, dx, dy):
        """
            Updates the Actor's Hitbox according to the Actor's change in direction.
        """
        self._limits[DIRECTIONS[0]] += dy
        self._limits[DIRECTIONS[1]] += dy
        self._limits[DIRECTIONS[2]] += dx
        self._limits[DIRECTIONS[3]] += dx

    def rotate_90(self):
        """
            Swap the width and height of the hitbox, represent a 90 turning of the hitbox
        """
        temp = self._height
        self._height = self._width
        self._width = temp
        # recalculate the size/shape
        self._limits = self.calculate_limits()

    def hit(self, other_hitbox):
        """
            Will check if the other Actor's Point position is within this Hitbox, and return if there has been a collison.
        """
        # Checks each side to see if they are in the same area
        if (self.left >= other_hitbox.right):
            self._is_hit = False
        elif (self.right <= other_hitbox.left):            
            self._is_hit = False
        elif (self.bottom <= other_hitbox.top):            
            self._is_hit = False
        elif (self.top >= other_hitbox.bottom):
            self._is_hit = False
        else:
            # Passes all checks, there is an overlap
            self._is_hit = True

        return self._is_hit

    def clicked(self, point):
        """
            Translates a point position into a Hitbox to check if hit
        """
        return self.hit(Hitbox(point, 0, 0))

    def get_is_hit(self):
        """
            Returns if the hitbox is colliding
        """
        return self._is_hit

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @property
    def top(self):
        return self._limits[DIRECTIONS[0]]

    @top.setter
    def top(self, top_limit):
        self._limits[DIRECTIONS[0]] = top_limit

    @property
    def bottom(self):
        return self._limits[DIRECTIONS[1]]

    @bottom.setter
    def bottom(self, bottom_limit):
        self._limits[DIRECTIONS[1]] = bottom_limit

    @property
    def left(self):
        return self._limits[DIRECTIONS[2]]

    @left.setter
    def set_left(self, left_limit):
        self._limits[DIRECTIONS[2]] = left_limit

    @property
    def right(self):
        return self._limits[DIRECTIONS[3]]

    @right.setter
    def right(self, right_limit):
        self._limits[DIRECTIONS[3]] = right_limit
