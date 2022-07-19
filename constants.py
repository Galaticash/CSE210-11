
from point import Point

# Because the game is grid-like, there are only four directions
#  Not currently used, I guess it's more of a guideline for
#  how all direction formats should be named and ordered (like in dictionaries)
# {"TOP": Exit(), "BOTTOM": Exit(), "LEFT": Exit(), "RIGHT": Exit()}
DIRECTIONS = ["TOP", "BOTTOM", "LEFT", "RIGHT"]
ROTATION = [0, 90, 180, 270]

# Window Size
WINDOW_MAX_X = 900
UI_Y_POS = 100 # The actual Scene is between 100 - 900
WINDOW_MAX_Y = 600

# The frame at which the animation frame is updated
UPDATE_FRAME = 5

## SIZE OF ACTORS/FONT IN PIXELS ##
FONT_SIZE = 30
COUNTER_SIZE = FONT_SIZE

# To account for extra blank pixels in the actor
# Note: The Player is 24 pixels/ Enemy 32 pixels, 
# but the sprites are upscaled up to be printed at this size
ACTOR_WIDTH = 80
ACTOR_HEIGHT = ACTOR_WIDTH
# int(ACTOR_WIDTH * 1.5)
ACTOR_SCALE = 1.25
ENEMY_SCALE = ACTOR_SCALE + .5

PICKUP_SIZE = 50

# Actor Names (VERY HARDCODED AND WEIRD)
PLAYER_NAME = "Player"
PLAYER_SPAWN = Point(300, 325)
#Point(450, 300)

## RELATIVE FILEPATHS FOR IMAGES ##

# NOTE: An idea I had, but not implemented
#SPRITE_SOURCE = "Astronaut\\"
#RUNNING = "Astronaut_Run"
#IDLE = "Astronaut_Idle"
#IMAGE_FILETYPE = ".png"

BLANK_ICON = "blank.png"
GEM_ICON = "OtherSprites\\Diamond.png"
BULLET_ICON = "OtherSprites\\EnergyPack.png"
HEALTH_ICON = "OtherSprites\\Heart.png"
LIFE_ICON = "OtherSprites\\LivesCounter.png"
KEY_ICON = "OtherSprites\\key.png"
SPACESHIP_ICON = "SmallDriller.png"
#"8-bit-space-ship.png"
ROCK_BLACK = "Rock\\rock_black.png"
ROCK_BLUE = "Rock\\rock_blue.png"

BOSS_BG = "possible_boss_fight_background.png"

GAME_TITLE = "Astronaut Adventure"

# When the Collision Actor is flung by a collision, how long until it can change its velocity
FREEZE_TIME = 15

AGGRO = ""

# Actor Constants
STEP_SIZE = 5
COLOR_TIMER_MAX = 2
INVULNERABLE_TIMER = 15

# Player Constants
STARTING_LIVES = 1 #3
PLAYER_HP = 25
STARTING_SHOTS = 75

# Boss Constants
BOSS_NAME = "Boss"
BOSS_HP = 40
BOSS_ATTACK = 10

ENEMY_NAME = "Enemy"

BOSS_KEY_NAME = "Boss_key"
HEALTH_NAME = "Health"
BULLET_NAME = "Bullet"
GEM_NAME = "Gem"
LIFE_NAME = "Life"

# How far the bullet spawns from the Player
BULLET_PADDING = 100
# Speed of the bullet
BULLET_SPEED = 5

# Game Over display
GAME_OVER_SIZE = FONT_SIZE * 2
BUTTON_SIZE = int(FONT_SIZE * 1.5)
# Replay buttons
BUTTON_PADDING = 0
BUTTON_COLOR = "GREEN"
BUTTON_TEXT_COLOR = "WHITE"