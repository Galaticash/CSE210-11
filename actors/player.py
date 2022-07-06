from actors.collision_actor import *
from player_input import Player_Input, pyray
from actors.score import Score

class Player(Collision_Actor):
    """
        The Player/Cycle that is controlled by the user.
    """
    def __init__(self, max_x, max_y, font_size, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)
        # Reset Base Color, Color, and Symbol
        self._base_color = Color("BLUE")
        self._color = copy.copy(self._base_color)
        self._symbol = "@"

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()

        # Player starts with an initial velocity of up.
        self._velocity = [0, -1]
        self._velocity_prev = self._velocity[:]

        # Overrite Spawn Point, Position
        self._spawn_point = Point(max_x, max_y, int(self._max_x * 1/3), self._max_y//2)
        self._position = self._spawn_point
        
        # Create a Score object
        self._score = Score(max_x, max_y, [int(self._max_x * 1/12), 0], self._font_size, "Player One:")

    def get_velocity(self):
        """
            Gets the current velocity of the Player. Relies on Player Input. 
            If Player Input is [0, 0], continues travelling in the previous direction.
        """
        self._velocity_prev = copy.copy(self._velocity)
        new_velocity = self._player_input.get_direction()
        
        # If there has been user input to change the direction,
        if not (new_velocity == [0, 0]):
            # Update the player to move the direction the user has specified.
            self._velocity = new_velocity
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
        self._velocity = [0, -1]
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