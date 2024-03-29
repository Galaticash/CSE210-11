from actors.collision_actor import *
from actors.Fighting_Actor import Fighting_Actor
from actors.bullet import Bullet
# For User Input
from player_input import Player_Input, pyray
# For Score/Inventory display
from actors.counter import Counter
# Constants
#  Inventory/Counter Icons
from constants import GEM_ICON, BULLET_ICON, HEALTH_ICON, LIFE_ICON
from constants import ACTOR_SCALE, COUNTER_SIZE, STARTING_LIVES, PLAYER_HP, STARTING_SHOTS, BULLET_PADDING, BULLET_SPEED, BOSS_KEY_NAME
from constants import GEM_NAME, LIFE_NAME, HEALTH_NAME, BULLET_NAME

from sound import Sound

class Player(Fighting_Actor):
    """
        The Player/Astronaut that is controlled by the user.
    """
    def __init__(self, name, position, width, height, audio_service, image="blank.png", color=HARD_COLORS["WHITE"]):
        super().__init__(name, position, width, height, image, color)
        self._max_HP = PLAYER_HP
        self._spawn_point = position
        self._audio_service = audio_service

        self._scale = ACTOR_SCALE

        # Overwrite the Images
        # TODO: Can adjust file order for animation to be less clunky?
        self._frames = ["Astronaut\\Astronaut_Idle3.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run2.png", "Astronaut\\Astronaut_Run1.png", "Astronaut\\Astronaut_Run3.png", "Astronaut\\Astronaut_Run4.png", "Astronaut\\Astronaut_Run5.png", "Astronaut\\Astronaut_Run6.png"]
        #assets\Astronaut\Astronaut_Run1.png

        # Give Player a Player_Input to determine velocity/movement
        self._player_input = Player_Input()
        self._velocity = [0, 0]

        # Create a Counter for each item
        self._lives = Counter(Point(50, COUNTER_SIZE), COUNTER_SIZE, "Lives:", LIFE_ICON)
        self._health = Counter(Point(150, COUNTER_SIZE), COUNTER_SIZE, "Health:", HEALTH_ICON)  
        self._gems = Counter(Point(375, COUNTER_SIZE), COUNTER_SIZE, "Gems:", GEM_ICON) 
        self._shots = Counter(Point(500, COUNTER_SIZE), COUNTER_SIZE, "Shots:", BULLET_ICON)
        self._key = Counter(Point(624, COUNTER_SIZE//2), COUNTER_SIZE, "Key: ")

        # DEBUG: Add to HUD to print [x, y] of Astronaut
        self._print_x = Counter(Point(750, COUNTER_SIZE), COUNTER_SIZE, "X")
        self._print_y = Counter(Point(750, COUNTER_SIZE *2), COUNTER_SIZE, "Y")

        self._HUD = [self._gems, self._lives, self._health, self._shots, self._key, self._print_x, self._print_y]

        # Initialize all the Player stats
        self.start_stats()

    def set_position(self, position):
        """
            Overrides the position of the Player.
        """
        self._position = position
        self._hitbox.overrite_position(self._position)

    def move(self):
        """
            Moves the Player, but also updates the x/y coordinate display
        """
        return_item = super().move()
        self._print_x.set_count(self._position.get_x())
        self._print_y.set_count(self._position.get_y())
        return return_item
    
    def has_key(self):
        """
            Returns if the Player has found the boss key.
        """
        return self._key.get_count() >= 1

    def start_stats(self):
        """
            Changes the Player's stats to the starting amounts.
        """
        self._alive = True
        self._velocity = [0, 0]
        self._current_HP = self._max_HP
        self._position = copy.copy(self._spawn_point) # TODO: Player doesn't reset position?
        
        # DEBUG: Set key <- 1 for immediate Boss fight
        self._key.set_count(0)
        self._gems.set_count(0)
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
                # Remove a shot and shoot it
                # DEBUG: Remove to get infinite gun
                self._shots.add(-1)
                return self.fire_bullet()
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
        return self._HUD

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
        bullet_width = int(self._width)
        bullet_height = int(self._width //3)
        self._audio_service.play_sound(Sound("boing.wav"))
        return Bullet("bullet", new_position, speed, bullet_width, bullet_height)

    def pickup(self, item):
        """
            The Player will pickup the given item.
        """
        if item.get_name()[0:-3] == BOSS_KEY_NAME:
            self._key.add(item.get_amount())
            #self._audio_service.play_sound(Sound("crab_rave.mp3"))
            self._audio_service.loop_sound(Sound("crab_rave.mp3"))
        elif item.get_name()[0:-3] == GEM_NAME:
            self._gems.add(item.get_amount())
        elif item.get_name()[0:-3] == BULLET_NAME:
            self._shots.add(item.get_amount())
        elif item.get_name()[0:-3] == HEALTH_NAME:
            self._update_HP(item.get_amount())
        elif item.get_name()[0:-3] == LIFE_NAME:
            self._lives.add(item.get_amount())
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
            self._update_HP(-1 * damage_points)
            if self._current_HP <= 0:
                if self._lives.get_count() > 0:
                    # Currently, lives is just a counter, 
                    #  doesn't have any in-game effect 
                    #  (send player to the front of the room,
                    #   respawn at the spaceship, etc)
                    self._lives.add(-1)                  
                    self._set_HP(self._max_HP)
                else:
                    # Game over
                    self._alive = False                      
                    # Make sure to display 0 as the minimum HP
                    self._set_HP(0)
                    self._color = Color(HARD_COLORS["NONE"][0], HARD_COLORS["NONE"][1], HARD_COLORS["NONE"][2], HARD_COLORS["NONE"][3])