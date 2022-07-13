from actors.collision_actor import *
from actors.image import Image

# NOTE: Currently testing with only one .png in position _frames[0]

# The frame at which the animation frame is updated
UPDATE_FRAME = 5

class Fighting_Actor(Collision_Actor):
    def __init__(self, position, size, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        # Health Points
        self._max_HP = 10
        self._current_HP = 10
        
        # For animation
        self._frame_counter = 0
        self._frames = ["Test_file", "1", "2", "3", "4", "5"]
        self._update_fame = UPDATE_FRAME
        self._current_frame = 0
        self._scale = 10
        self._facing_right = True
        self._rotation = 0

        # Base Color, and current Color
        self._base_color = Color(color)
        self._color = copy.copy(self._base_color)

        # TODO: Player will do damage with a weapon (for Player -> 0, but their weapon)
        # How much damage is done to the other collider
        self._collision_damage = 1

    def get_frame(self):
        """
            Animates the character, returns the current frame.
        """
        # If the Actor is standing still, stay on first frame (idle)
        # Also if the Actor only has one animation frame/sprite
        if self._velocity == [0, 0] or len(self._frames) == 1:
            return self._frames[0]

        # Check for the update frame
        self._frame_counter += 1
        if self._frame_counter == self._update_fame:
            # Reset the counter and update the animation frame,
            #  making sure to loop when it hits the end.
            self._frame_counter = 0
            self._current_frame += 1
            if self._current_frame == len(self._frames):
                self._current_frame = 1
        # Return the filepath of the current frame
        return self._frames[self._current_frame]

    def get_display(self):
        """
            Returns the frame of the Actor to display.
        """
        # Create and return an Image (the filepath, scale, and rotation)
        texture = self.get_frame()
        direction = self.get_velocity()
        if direction[0] < 0:
            # Going Left
            #self._rotation = 180
            self._scale = abs(self._scale) * -1
        elif direction[0] > 0:
            # Going Right
            #self._rotation = 0
            self._scale = abs(self._scale)
        return Image(texture, self._scale, self._rotation, self._color)