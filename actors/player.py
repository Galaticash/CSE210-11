from actors.collision_actor import *
from actors.Fighting_Actor import Fighting_Actor
from actors.bullet import Bullet
# For User Input
from player_input import Player_Input, pyray
# For Score/Inventory display
from actors.counter import Counter

# TODO: Move to constants file

STARTING_LIVES = 3
STARTING_SHOTS = 5
BULLET_TIMER = 10

# NOTE: Not implemented
SPRITE_SOURCE = "Astronaut\\"
RUNNING = "Astronaut_Run"
IDLE = "Astronaut_Idle"
IMAGE_FILETYPE = ".png"

BULLET_PADDING = 100
BULLET_SPEED = 5

class Player(Fighting_Actor):
    """
        The Player/Astronaut that is controlled by the user.
    """
    def __init__(self, name, position, size, image="blank.png", color="WHITE"):
        super().__init__(name, position, size, image, color)

        # Overwrite the Images
        # TODO: Can adjust file order for animation to be less clunky?
        self._frames = ["Astronaut\\Astronaut_Idle3.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run2.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run3.png", "Astronaut\\Astronaut_Run4.png", "Astronaut\\Astronaut_Run5.png", "Astronaut\\Astronaut_Run6.png"]
        #assets\Astronaut\Astronaut_Run1.png

        self._shot_reloading = False
        self._bullet_timer = 0
        self._bullet_reset = BULLET_TIMER

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()
        self._velocity = [0, 0]

        # TODO: Change to UI/inventory?
        # Create a Counter for each item
        self._gems = Counter(Point(FONT_SIZE *2, 0), FONT_SIZE, "Gems:")
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
        """
            Checks if the Player is shooting.
        """
        # If the user pressed the "shoot" button
        if self._player_input.get_shoot():
            # If there are any bullets to shoot
            if self._shots.get_count() > 0:
                # If the reload time has passed
                if not(self._shot_reloading):                    
                    # Start reload timer
                    self._shot_reloading = True
                    # Remove a shot and shoot it
                    # DEBUG: Infinite gun
                    # self._shots.add(-1)
                    return self.fire_bullet()
                else:
                    self._bullet_timer += 1
                    if self._bullet_timer >= self._bullet_reset:
                        self._bullet_timer = 0
                        self._shot_reloading = False
                    return False
            else:
                # out of bullets, sound cue?
                 return False
        else:
            return False

    def get_velocity(self):
        """
            Gets the current velocity of the Player. Relies on Player Input.
        """
        if self._movement_control:
            # Update the player to move the direction the user has specified.
            self._velocity = self._player_input.get_direction()
        else:
            self.override_update()
        return super().get_velocity()

    def respawn(self):
        """
            Respawns the Player at their Spawn Point.
        """
        self.start_stats()

        # Copy by value only.
        self._position = copy.copy(self._spawn_point)
        self._velocity = [0, 0]
        self.reset_color()

    def win(self):
        """
            What happens when the Player wins - not needed?
        """
        pass

    def get_HUD(self):
        """
            Returns the Player's HUD objects.
        """
        return [self._gems, self._health, self._lives, self._shots]

    def fire_bullet(self):
        """
            Fires a bullet in front of the Player.
        """
        # Puts the Bullet a certain space away from the shooter
        # Math differs based on facing direction
        new_position = copy.copy(self._position)
        padding = BULLET_PADDING
        speed = [0, 0]

        # If facing left or right
        if not (self._facing[0] == 0):
            if self._facing[0] < 0:
                padding *= -1
            new_position.add_velocity(padding, 0)
            speed = [self._facing[0] * BULLET_SPEED, 0]
        # If facing up or down
        elif not (self._facing[1] == 0):   
            if self._facing[1] < 0:
                padding *= -1         
            new_position.add_velocity(0, padding)
            speed = [0, self._facing[1] * BULLET_SPEED]

        # Returns the bullet back to the Scene Manager so 
        #  it can display it and detect collisions
        return Bullet("bullet", new_position, speed, self._size)

    def pickup(self, item):
        """
            The Player will pickup the given item.
        """
        # print(f"Player should pickup {item.get_name()}")
        if item.get_name() == "Gem_p":
            self._gems.add(item.get_amount())
        elif item.get_name() == "Bullet_p":
            self._shots.add(item.get_amount())
        else:
            print("Unidentified Item")

    def _set_HP(self, new_HP):
        """
            Changes the current HP and its display
        """
        self._current_HP = new_HP
        self._health.set_count(new_HP)

    def _update_HP(self, points):
        """
            Adds points to the HP and its display.
        """
        self._current_HP += points
        self._health.add(points)

    def damage(self, damage_points):
        """
            Damages the Player based on the damage_points from what hit it.
            Player overrides because of lives system and Player death
                is a game over condition.
        """
        # If ther HP isn't already 0
        if self._current_HP >= 0:
            self._update_HP(damage_points)
            if self._current_HP <= 0:
                if self._lives.get_count() > 0:
                    self._lives.add(-1)
                    self._set_HP(self._max_HP)
                else:
                    # Game over
                    # Make sure to display 0 as the minimum HP
                    self._set_HP(0)
                    self._color = Color("INVISIBLE")