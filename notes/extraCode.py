
    # def _set_limits(self):
    #     # The position is at the Top Left (determined by python.draw_text/etc)
    #     self._limits[DIRECTIONS[0]] = (self._position.get_y() - self._size//2) - self._padding
    #     self._limits[DIRECTIONS[2]] = (self._position.get_x() - (self._size//2)) - self._padding

    #     # Top point + (down) font_size = Bottom point
    #     self._limits[DIRECTIONS[1]] = (self._position.get_y() + self._size//2) + self._padding

    #     # Left point + (right) font_size * width = Right point
    #     # The right side of the hitbox must be adjusted to the length of the symbol
    #     self._limits[DIRECTIONS[3]] = (self._position.get_x() + (self._size//2)) + self._padding

        # How many pixels the Actor travels per Move method call.
