
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

GAME_TITLE = "Astronaut Adventure"

# When the Collision Actor is flung by a collision, how long until it can change its velocity
FREEZE_TIME = 15

AGGRO = ""

# Actor Constants
STEP_SIZE = 5
COLOR_TIMER_MAX = 2
INVULNERABLE_TIMER = 15

# Player Constants
STARTING_LIVES = 1
PLAYER_HP = 25
STARTING_SHOTS = 50

# Boss Constants
BOSS_NAME = "Boss"
BOSS_HP = 40
BOSS_ATTACK = 10

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

## Scene Manager Constants ##
from actors.background_obj import collidable_obj
from actors.exit import Exit
# Scene bounds (all the same)
SCENE_EDGES = {"TOP": UI_Y_POS, "BOTTOM": WINDOW_MAX_Y, "LEFT": 0, "RIGHT": WINDOW_MAX_X}
# NOTE: Some funky math for the left/right edges, it goes wrong somewhere, but I was able to adjust it here (//2)
EXIT_POSITIONS = {"TOP": Point((SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"])//2, SCENE_EDGES["TOP"]), "BOTTOM": Point((SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"])//2, SCENE_EDGES["BOTTOM"]), "LEFT": Point(SCENE_EDGES["LEFT"], (SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"])//2 +  SCENE_EDGES["TOP"]), "RIGHT": Point(SCENE_EDGES["RIGHT"], (SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"])//2 + SCENE_EDGES["TOP"])}

# The widths and heights for each Exit/Edge
WALL_WIDTH = {"TOP": SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"], "BOTTOM": SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"], "LEFT": 0, "RIGHT": 0}
WALL_HEIGHT = {"TOP": 0, "BOTTOM": 0, "LEFT": SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"], "RIGHT": SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"]}

# The exits that, when collided with, move the Player to the next scene
EXITS =  {"TOP": Exit("TOP", EXIT_POSITIONS["TOP"], WALL_WIDTH["TOP"], WALL_HEIGHT["TOP"]), "LEFT": Exit("LEFT", EXIT_POSITIONS["LEFT"], WALL_WIDTH["LEFT"], WALL_HEIGHT["LEFT"]), "RIGHT": Exit("RIGHT", EXIT_POSITIONS["RIGHT"], WALL_WIDTH["RIGHT"], WALL_HEIGHT["RIGHT"]), "BOTTOM": Exit("BOTTOM", EXIT_POSITIONS["BOTTOM"], WALL_WIDTH["BOTTOM"], WALL_HEIGHT["BOTTOM"])}

# Blockers are placed if there is no connection (so they can't walk off the screen)
EXIT_BLOCKERS = {"TOP": collidable_obj("TOP_WALL", EXIT_POSITIONS["TOP"], WALL_WIDTH["TOP"], WALL_HEIGHT["TOP"]), "BOTTOM": collidable_obj("BOTTOM_WALL", EXIT_POSITIONS["BOTTOM"], WALL_WIDTH["BOTTOM"], WALL_HEIGHT["BOTTOM"]), "LEFT": collidable_obj("LEFT_WALL", EXIT_POSITIONS["LEFT"], WALL_WIDTH["LEFT"], WALL_HEIGHT["LEFT"]), "RIGHT": collidable_obj("RIGHT_WALL", EXIT_POSITIONS["RIGHT"], WALL_WIDTH["RIGHT"], WALL_HEIGHT["RIGHT"])}

# Where the Player enters the next Scene
ENTRANCE_PADDING = ACTOR_WIDTH + 25
ENTRANCE_POINTS = {"TOP": Point(EXIT_POSITIONS["TOP"].get_x(), EXIT_POSITIONS["TOP"].get_y() + ENTRANCE_PADDING),"BOTTOM": Point(EXIT_POSITIONS["BOTTOM"].get_x(), EXIT_POSITIONS["BOTTOM"].get_y() - ENTRANCE_PADDING), "LEFT": Point(EXIT_POSITIONS["LEFT"].get_x() + ENTRANCE_PADDING, EXIT_POSITIONS["LEFT"].get_y()), "RIGHT": Point(EXIT_POSITIONS["RIGHT"].get_x() - ENTRANCE_PADDING, EXIT_POSITIONS["RIGHT"].get_y())}