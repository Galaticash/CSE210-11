
# Because the game is grid-like, the directions things can face, and Scene connections
DIRECTIONS = ["TOP", "BOTTOM", "LEFT", "RIGHT"] 
# Not currently used, I guess it's more of a guideline for
#  how all direction formats should be named and ordered

# Because the game is grid-like, these are the rotations the Actors can be
#   currently only used for image rotation
ROTATION = [0, 90, 180, 270]

# Window Size
WINDOW_MAX_X = 900
UI_Y_POS = 100 # So the scene working space is between 100 - 900
WINDOW_MAX_Y = 600

# Actor/Font Sizing
FONT_SIZE = 30
# Note: The Player is 24 pixels/ Enemy 32 pixels, 
# but the sprites are upscaled up to be printed at this size
ACTOR_SIZE = 100
PICKUP_SIZE = ACTOR_SIZE //2

# Actor Names (VERY HARDCODED AND WEIRD)
PLAYER_NAME = "Player"

# Image locations
BLANK_ICON = "blank.png"
GEM_ICON = "OtherSprites\\Diamond.png"
BULLET_ICON = "OtherSprites\\EnergyPack.png"
HEALTH_ICON = "OtherSprites\\Heart.png"
LIFE_ICON = "OtherSprites\\LivesCounter.png"
KEY_ICON = "OtherSprites\\Diamond.png"

SPACESHIP_ICON = "SmallDriller.png"
#"8-bit-space-ship.png"
ROCK_BLACK = "Rock\\rock_black.png"
ROCK_BLUE = "Rock\\rock_blue.png"

# When the Collision Actor is flung by a collision, how long until it can change its velocity
FREEZE_TIME = 15

# Player Constants
STARTING_LIVES = 0 #3
PLAYER_HP = 5 #25
STARTING_SHOTS = 50

# Boss Constants
BOSS_HP = 40
BOSS_ATTACK = 10

# NOTE: Not implemented
#SPRITE_SOURCE = "Astronaut\\"
#RUNNING = "Astronaut_Run"
#IDLE = "Astronaut_Idle"
#IMAGE_FILETYPE = ".png"

# How far the bullet spawns from the Player
BULLET_PADDING = 100
# Speed of the bullet
BULLET_SPEED = 5


# Game Over display
GAME_OVER_SIZE = FONT_SIZE * 2
BUTTON_SIZE = int(FONT_SIZE * 1.5)