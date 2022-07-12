from actors.collision_actor import *
from player_input import Player_Input, pyray
from actors.score import Score
from actors.Fighting_Actor import Fighting_Actor
from director import FONT_SIZE

class Player(Fighting_Actor):
    """
        The Player/Cycle that is controlled by the user.
    """
    def __init__(self, max_x, max_y, size, image="", color="WHITE"):
        super().__init__(max_x, max_y, size, image, color)
        # Reset Base Color, Color, and Symbol
        self._base_color = Color("WHITE")
        self._color = copy.copy(self._base_color)

        # Overrite the Images
        self._frames = ["diamond1_2.png"]
        self._scale = 10

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()
        self._velocity = [0, 0]

        # Overrite Spawn Point, Position
        self._spawn_point = Point(max_x, max_y, int(self._max_x * 1/3), self._max_y//2)
        # TODO: Hmm Put spawn point as a passable variable to Actor?
        self._position = self._spawn_point
        top = (self._position.get_y() - self._size//2)
        bottom = (self._position.get_y() + self._size//2) 
        left = (self._position.get_x() - (self._size//2)) 
        right = (self._position.get_x() + (self._size//2)) 
        self._hitbox = Hitbox(top, bottom, left, right)
        
        # TODO: Change to UI/inventory?
        # Create a Score object
        self._score = Score(max_x, max_y, [int(self._max_x * 1/12), 0], FONT_SIZE, "Score:")

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
        print("player color change")
        self._color = Color(color)