from actors.collision_actor import Collision_Actor

# The frame at which the animation frame is updated
UPDATE_FRAME = 10

class Fighting_Actor(Collision_Actor):
    def __init__(self, max_x, max_y, size, image="", color="WHITE"):
        super().__init__(max_x, max_y, size, image, color)
        # Health Points
        self._max_HP = 10
        self._current_HP = 10
        
        # For animation
        self._frame_counter = 0
        self._frames = ["0", "1", "2", "3", "4", "5"]
        self._current_frame = 0

        # TODO: Player will do damage with a weapon (for Player -> 0, but their weapon)
        # How much damage is done to the other collider
        self._collision_damage = 1

    def get_frame(self):
        """
            Animates the character
        """
        if self._velocity == [0, 0]:
            return self._frames[0]
        # TODO: only change the frame every few refreshes
        self._frame_counter += 1
        if self._frame_counter == UPDATE_FRAME:
            self._frame_counter = 0
            self._current_frame += 1
            if self._current_frame == len(self._frames):
                self._current_frame = 0
            # TODO: Check the frame number
        return self._frames[self._current_frame]

    def get_display(self):
        # DEBUG: Temporary override
        return self.get_frame()