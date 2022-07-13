from actors.Fighting_Actor import *
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

class Player(Fighting_Actor):
    """
        The Player/Astronaut that is controlled by the user.
    """
    def __init__(self, position, size, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        # Overwrite the Images
        # TODO: Can adjust file order for animation to be less clunky?
        self._frames = ["Astronaut\\Astronaut_Idle3.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run2.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run3.png", "Astronaut\\Astronaut_Run4.png", "Astronaut\\Astronaut_Run5.png", "Astronaut\\Astronaut_Run6.png"]
        #assets\Astronaut\Astronaut_Run1.png

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()
        self._velocity = [0, 0]

        # Overrite Spawn Point, Position
        self._position = self._spawn_point
        top = (self._position.get_y() - self._size//2)
        bottom = (self._position.get_y() + self._size//2) 
        left = (self._position.get_x() - (self._size//2)) 
        right = (self._position.get_x() + (self._size//2)) 
        self._hitbox = Hitbox(top, bottom, left, right)
        
        # TODO: Change to UI/inventory?
        # Create a Score object
        self._score = Score(Point(FONT_SIZE *2, 0), FONT_SIZE, "Score:")

    def get_velocity(self):
        """
            Gets the current velocity of the Player. Relies on Player Input.
        """
        # Update the player to move the direction the user has specified.
        self._velocity = self._player_input.get_direction()
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