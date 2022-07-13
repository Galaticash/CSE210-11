from math import fabs
from actors.Fighting_Actor import *
from actors.bullet import Bullet
# For User Input
from player_input import Player_Input, pyray
# For Score/Inventory display
from actors.score import Score
from director import FONT_SIZE

# NOTE: Not implemented
SPRITE_SOURCE = "Astronaut\\"
RUNNING = "Astronaut_Run"
IDLE = "Astronaut_Idle"
IMAGE_FILETYPE = ".png"

BULLET_PADDING = 10

class Player(Fighting_Actor):
    """
        The Player/Astronaut that is controlled by the user.
    """
    def __init__(self, name, position, size, image="", color="WHITE"):
        super().__init__(name, position, size, image, color)
        # Overwrite the Images
        # TODO: Can adjust file order for animation to be less clunky?
        self._frames = ["Astronaut\\Astronaut_Idle3.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run2.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run3.png", "Astronaut\\Astronaut_Run4.png", "Astronaut\\Astronaut_Run5.png", "Astronaut\\Astronaut_Run6.png"]
        #assets\Astronaut\Astronaut_Run1.png

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()
        self._velocity = [0, 0]
        self._facing = [1, 0]

        # TODO: Change to UI/inventory?
        # Create a Score object
        self._score = Score(Point(FONT_SIZE *2, 0), FONT_SIZE, "Score:")

    def check_shoot(self):
        if self._player_input.get_shoot():
            self.fire_bullet()

    def get_velocity(self):
        """
            Gets the current velocity of the Player. Relies on Player Input.
        """
        # Update the player to move the direction the user has specified.
        self._velocity = self._player_input.get_direction()
        if not (self._velocity == [0, 0]):
            self._facing = self._velocity
        return self._velocity

    def move(self):
        """
            Moves the Player based on keyboard input, 
             loops to other side of the screen (in Point class).
        """
        super().move()

    def respawn(self):
        """
            Respawns the Player at their Spawn Point.
        """
        # Copy by value only.
        self._position = copy.copy(self._spawn_point)
        self._velocity = [0, 0]
        self.reset_color()

    def win(self):
        """
            Adds points to the Player's score based on what it hit.
        """
        self._score.add_points(1)

    def get_score(self):
        """
            Returns the Player's Score object.
        """
        return self._score

    def set_color(self, color):
        """
            Sets the color of the Player.
        """
        self._color = Color(color)

    def fire_bullet(self):
        new_position = copy.copy(self._position)
        padding = BULLET_PADDING
        # If facing left or right
        if not (self._facing[0] == 0):
            new_position.add_velocity(padding, 0)
        # If facing up or down
        elif not (self._facing[1] == 0):            
            new_position.add_velocity(0, padding)

        new_bullet = Bullet("bullet", new_position, self._facing, self._size//2)

    def damage(self, damage_points):
        if self._current_HP >= 0:
            self._current_HP -= damage_points
            if self._current_HP <= 0:
                # Game Over
                self._color = Color("INVISIBLE")