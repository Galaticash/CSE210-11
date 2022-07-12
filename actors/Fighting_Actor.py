from actors.collision_actor import Collision_Actor
from actors.image import Image

# NOTE: Currently testing with only one .png in position _frames[0]

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
        self._frames = ["Test_file", "1", "2", "3", "4", "5"]
        self._current_frame = 0
        self._scale = 1
        self._rotation = 0

        # TODO: Player will do damage with a weapon (for Player -> 0, but their weapon)
        # How much damage is done to the other collider
        self._collision_damage = 1

    def get_frame(self):
        """
            Animates the character, returns the current frame.
        """
        # If the Player is standing still, stay on first frame
        if self._velocity == [0, 0]:
            return self._frames[0]

        # Check for the update frame
        self._frame_counter += 1
        if self._frame_counter == UPDATE_FRAME:
            # Reset the counter and update the animation frame,
            #  making sure to loop when it hits the end.
            self._frame_counter = 0
            #self._current_frame += 1
            if self._current_frame == len(self._frames):
                self._current_frame = 1
        # Return the filepath of the current frame
        return self._frames[self._current_frame]

    def get_display(self):
        """
            Returns the frame of the Actor to display.
        """
        # Create and return an Image (the filepath, scale, and rotation)
        return Image(self.get_frame(), self._scale, self._rotation)