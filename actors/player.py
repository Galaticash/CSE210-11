from math import fabs
from actors.Fighting_Actor import *
from actors.bullet import Bullet
# For User Input
from player_input import Player_Input, pyray
# For Score/Inventory display
from actors.counter import Counter
from director import FONT_SIZE

STARTING_LIVES = 3
STARTING_SHOTS = 5


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
        # Create a Counter for each item
        self._score = Counter(Point(FONT_SIZE *2, 0), FONT_SIZE, "Score:")
        self._lives = Counter(Point(FONT_SIZE *2, FONT_SIZE), FONT_SIZE, "Lives:")
        self._health = Counter(Point(FONT_SIZE *2, FONT_SIZE *2), FONT_SIZE, "Health:")   
        self._shots = Counter(Point(FONT_SIZE *2, FONT_SIZE *3), FONT_SIZE, "Shots:")

        # Initialize all the Player stats
        self.start_stats()

    def start_stats(self):
        """
            Changes the Player's stats to the starting amounts
            Assumes all stat counters start at 0
        """
        self._current_HP = self._max_HP
        self._lives.set_count(STARTING_LIVES)
        self._health.set_count(self._current_HP)
        self._shots.set_count(STARTING_SHOTS)

    def check_shoot(self):
        if self._player_input.get_shoot():
            if self._shots.get_count() > 0:
                self.fire_bullet()
            else:
                # out of bullets, sound cue?
                pass

    def get_velocity(self):
        """
            Gets the current velocity of the Player. Relies on Player Input.
        """
        if self._movement_control:
            # Update the player to move the direction the user has specified.
            self._velocity = self._player_input.get_direction()
            if not (self._velocity == [0, 0]):
                self._facing = self._velocity
            return self._velocity
        else:
            # Update the time until the user regains control
            self._control_timer += 1
            if self._control_timer >= self._control_reset:
                self._movement_control = True

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

    def get_HUD(self):
        """
            Returns the Player's HUD objects.
        """
        return [self._score, self._health, self._lives, self._shots]

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

    def _set_HP(self, new_HP):
        self._current_HP = new_HP
        self._health.set_count(new_HP)

    def _update_HP(self, points):
        self._current_HP += points
        self._health.add(points)

    def damage(self, damage_points):
        if self._current_HP >= 0:
            self._update_HP(-1 * damage_points)
            if self._current_HP <= 0:
                if self._lives.get_count() > 0:
                    self._lives.add(-1)
                    self._set_HP(self._max_HP)
                else:
                    # Game over
                    # Make sure to display 0 as the minimum HP
                    self._set_HP(0)
                    self._color = Color("INVISIBLE")