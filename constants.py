DIRECTIONS = ["TOP", "BOTTOM", "LEFT", "RIGHT"] 
# Not currently used, I guess it's more of a guideline for
#  how all direction formats should be named and ordered

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

# Actor Names
PLAYER_NAME = "Player"

# Icons
GEM_ICON = "OtherSprites\\Diamond.png"
BULLET_ICON = "OtherSprites\\EnergyPack.png"
HEALTH_ICON = "OtherSprites\\Heart.png"
LIFE_ICON = "OtherSprites\\LivesCounter.png"


# When the Collision Actor is flung by a collision, how long until it can change its velocity
FREEZE_TIME = 15


# Player Constants
STARTING_LIVES = 3
STARTING_SHOTS = 5

# NOTE: Not implemented
#SPRITE_SOURCE = "Astronaut\\"
#RUNNING = "Astronaut_Run"
#IDLE = "Astronaut_Idle"
#IMAGE_FILETYPE = ".png"

BULLET_PADDING = 100
BULLET_SPEED = 5
