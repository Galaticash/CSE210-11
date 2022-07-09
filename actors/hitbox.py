class Hitbox():
    """
        A 2D Hitbox that determines if a Point position is within it's bounds.
    """
    def __init__(self, width, size, padding = 0):
        # The bounds of the Hitbox
        self._hitbox = {"Top": 0, "Bottom": 0, "Right": 0, "Left": 0}
        
        # Width is the length (w/o font size included)
        self._width = width
        # The size of the symbol/hitbox
        self._size = size
        # The extra pixels of padding for the hitbox.
        self._padding = padding
        self._is_hit = False
    
    def update(self, position):
        """
            Updates the Actor's hitbox according to the given position Point.
        """
        # The position is at the Top Left (determined by python.draw_text/etc)
        self._hitbox["Top"] = position.get_y() - self._padding
        # position.get_y() - self._size//2 
        self._hitbox["Left"] = position.get_x() - self._padding
        # position.get_x() - self._size//2 
        #

        # Top point + (down) font_size = Bottom point
        self._hitbox["Bottom"] = (position.get_y() + self._size) + self._padding
        # position.get_y() + self._size//2 
        #

        # Left point + (right) font_size * width = Right point
        # The right side of the hitbox must be adjusted to the length of the symbol
        self._hitbox["Right"] = (position.get_x() + (self._width * self._size)) + self._padding
        # position.get_x() + self._size//2 
        #

    def hit(self, other_collider_pos):
        """
            Will check if the other Actor's Point position is within this Hitbox, and return if there has been a collison.
        """
        # If the Point position is within ALL of the bounds
        if other_collider_pos.get_y() >= self._hitbox["Top"]:
            if other_collider_pos.get_y() <= self._hitbox["Bottom"]:
                if other_collider_pos.get_x() >= self._hitbox["Left"]:
                    if other_collider_pos.get_x() <= self._hitbox["Right"]:
                        self._is_hit = True
        else:
            self._is_hit = False
            
        return self._is_hit

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
        return self._hitbox["Top"]

    @top.setter
    def top(self, top_limit):
        self._hitbox["Top"] = top_limit
        self._width = 1

    @property
    def bottom(self):
        return self._hitbox["Bottom"]

    @bottom.setter
    def bottom(self, bottom_limit):
        self._hitbox["Bottom"] = bottom_limit
    
    @property
    def right(self):
        return self._hitbox["Right"]

    @right.setter
    def right(self, right_limit):
        self._hitbox["Right"] = right_limit

    @property
    def left(self):
        return self._hitbox["Left"]

    @left.setter
    def set_left(self, left_limit):
        self._hitbox["Left"] = left_limit