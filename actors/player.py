from actors.collision_actor import *
from player_input import Player_Input, pyray
from actors.score import Score
from actors.Fighting_Actor import Fighting_Actor

UPDATE_FRAME = 10

class Player(Fighting_Actor):
    """
        The Player/Cycle that is controlled by the user.
    """
    def __init__(self, max_x, max_y, size, image="", color="WHITE"):
        super().__init__(max_x, max_y, size, image, color)
        # Reset Base Color, Color, and Symbol
        self._base_color = Color("WHITE")
        self._color = copy.copy(self._base_color)

        # For animation TODO: move to Fighting Actor to animate both Enemy and Player
        self._frame_counter = 0
        self._frames = ["0", "1", "2", "3", "4", "5"]
        self._current_frame = 0
        self._symbol = "@"


        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()
        self._velocity = [0, 0]

        # Overrite Spawn Point, Position
        self._spawn_point = Point(max_x, max_y, int(self._max_x * 1/3), self._max_y//2)
        self._position = self._spawn_point
        
        # Create a Score object
        self._score = Score(max_x, max_y, [int(self._max_x * 1/12), 0], self._size, "Player One:")

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