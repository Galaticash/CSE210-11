from actors.enemy import Enemy, Point
from actors.Boss import Boss
from actors.hitbox import Hitbox
from actors.background_obj import background_obj, collidable_obj, long_object
from constants import ACTOR_HEIGHT, ACTOR_WIDTH, PICKUP_SIZE, ROCK_BLACK, ROCK_BLUE, SPACESHIP_ICON, WINDOW_MAX_X, WINDOW_MAX_Y, BOSS_NAME, BOSS_KEY_NAME, AGGRO, HEALTH_NAME, BULLET_NAME, GEM_NAME
from actors.pickup import *

"""
    TODO: Add all the items, Enemies, Boss to the things in a scene
        can do enemies = [Enemy(...), Enemy(...) ...] or 
        use .append() to shorten how wide the code is (easier to read, edit)
"""

WALL_SIZE = 400
PADDING = 50

class Scene():
    """
        An object that holds a list of all the types of Actors within an area.
        Also knows if there is a scene connected in a direction.
    """
    def __init__(self):
        self._name = "None"
        # The Enemies that the Player has to battle
        self._enemies = []
        self._hidden_enemies = []

        # Rocks, barriers, barrels
        # Just anything the Player can collide with (non-fighting)
        # Object Parameters - Position (Top, Bottom, Left, Right) or XY coordinate for TL/BR, color
        self._objects = []

        # Images to add a little more life to the scene
        self._bg_objects = []
        self._fore_objects = []

        # The areas where the Player can ENTER the scene - obsolete?
        # TODO: Where the Player is sent when they enter the scene
        self._enter_areas = {"TOP": None, "BOTTOM": None, "LEFT": None, "RIGHT": None}
        
        # The connected Scenes in each direction
        self._connections = {"TOP": None, "BOTTOM": None, "LEFT": None, "RIGHT": None}

    def get_name(self):
        """
            Returns the name of the scene - obsolete?
        """
        return self._name

    def add_connection(self, direction, scene):
        """
            Add a connection to the current scene given a direction and a scene.
        """
        self._connections[direction] = scene
        #self._enter_areas[direction] = 

    def get_connection(self, direction):
        """
            Returns the scene that is connected in the given direction.
        """
        return self._connections[direction]

    def get_enemies(self):
        """
            Returns the list of enemies.
        """
        return self._enemies

    def get_objects(self):
        """
            Returns the list of colliders (non-fighting)
        """
        return self._objects

    def get_bg_objects(self):
        """
            Returns the background objects (simply images)
        """
        return self._bg_objects

    def get_fore_objects(self):
        """
            Returns the foreground objects (simply images)
        """
        return self._fore_objects

    def get_hidden_enemies(self):
        """
            Returns the hidden enemies in the scene (reveal themselves when event triggered)
        """
        return self._hidden_enemies

class Spawn_scene(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Spawn"

        #self._objects.append(Pickup(BOSS_KEY_NAME + str(1), Point(450, 300), 1, PICKUP_SIZE))        
        #self._objects.append(Pickup(BULLET_NAME + str(2), Point(450, 400), 1, PICKUP_SIZE))
        #self._objects.append(Pickup(HEALTH_NAME + str(1), Point(450, 500), 1, PICKUP_SIZE))
        
        # There will be no enemies in the Spawn scene
        #self._enemies = []
        
        # Hitboxes that are not square will result in LOTS of errors, so only square things lol
        #self._objects.append(long_object("topWall1", Point(ACTOR_WIDTH * 2, ACTOR_WIDTH), WALL_SIZE, ROCK_BLACK_LONG, 0, 1.25))
        #self._objects.append(long_object("topWall1", Point(900 - ACTOR_WIDTH * 2, 100), WALL_SIZE, ROCK_BLACK_LONG, 1.25))
        
        self._fore_objects.append(background_obj(Point(20, 300), int(WALL_SIZE * 2/3), ROCK_BLUE))

        self._objects.append(collidable_obj("topWall1", Point(WALL_SIZE//2 - PADDING, 0), WALL_SIZE, WALL_SIZE, ROCK_BLACK))
        self._objects.append(collidable_obj("topWall2", Point(900 - WALL_SIZE//2 + PADDING, 0), WALL_SIZE, WALL_SIZE, ROCK_BLACK))

        self._objects.append(collidable_obj("bottomWall1", Point(WALL_SIZE//2 - PADDING, 600), WALL_SIZE, WALL_SIZE, ROCK_BLACK))
        self._objects.append(collidable_obj("bottomWall2", Point(900 - WALL_SIZE//2 + PADDING, 600), WALL_SIZE, WALL_SIZE, ROCK_BLACK))

        #self._objects.append(collidable_obj("topWall2", Point(100, 300), ACTOR_WIDTH, ROCK_BLACK_LONG))
        #self._objects.append(collidable_obj("topWall3", Point(500, 500), ACTOR_WIDTH, ROCK_BLUE_LONG))
        
        self._bg_objects.append(background_obj(Point(300, 300), ACTOR_WIDTH, SPACESHIP_ICON, 75, 1))

        #self._objects = [collidable_obj("Wall", Point(450, 100), ACTOR_WIDTH)]

class Scene1(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Right"
        self._enemies = [Enemy("Enemy1", Point(100, 100), ACTOR_WIDTH, ACTOR_HEIGHT), Enemy("Enemy2", Point(400, 400), ACTOR_WIDTH, ACTOR_HEIGHT)]

        self._objects = [collidable_obj("Wall", Point(450, 100), ACTOR_WIDTH, ACTOR_WIDTH)]

class Scene2(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Down"
        self._enemies.append(Enemy("enemy1", Point(100, 650), ACTOR_WIDTH, ACTOR_HEIGHT, [Point(650, 100), Point(650, 300)]))
        self._enemies.append(Enemy("enemy2", Point(200, 400), ACTOR_WIDTH, ACTOR_HEIGHT, [Point(400, 400), Point(200, 400)]))
        self._enemies.append(Enemy("enemy3", Point(150, 200), ACTOR_WIDTH, ACTOR_HEIGHT, [Point(350, 200), Point(150, 200)]))

class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Test"

        # Adds enemies, treated as colliders with movement
        self._enemies = [Enemy("Enemy1", Point(int(WINDOW_MAX_X * 2/3) - 5, WINDOW_MAX_Y//2), ACTOR_WIDTH, ACTOR_HEIGHT), Enemy("Enemy2", Point(int(WINDOW_MAX_X * 1/3), WINDOW_MAX_Y//2), ACTOR_WIDTH, ACTOR_HEIGHT), Enemy("Enemy3", Point(int(WINDOW_MAX_X * 2/3) + 75, WINDOW_MAX_Y//2), ACTOR_WIDTH, ACTOR_HEIGHT), Enemy("Enemy4", Point(int(WINDOW_MAX_X * 1/3) - 75, WINDOW_MAX_Y//2), ACTOR_WIDTH, ACTOR_HEIGHT)]        
        #self._scene_manager.add_enemy(Enemy("Enemy5", Point(200a, 200), self._actor_size, [Point(450, 200), Point(550, 200)]))
        
        # Adds the pickups and other non-moving collidables
        # Things that do collide but DON'T move  
        # Infinity hahaha
        self._objects = [collidable_obj("Rock", Point(650, 500), ACTOR_WIDTH, ACTOR_WIDTH, ROCK_BLACK), ReusablePickup("Gem", Point(300, 150), 5, PICKUP_SIZE), ReusablePickup("Life", Point(400, 150), 1, PICKUP_SIZE), ReusablePickup("Heart", Point(500, 150), 10, PICKUP_SIZE), ReusablePickup("Bullet", Point(600, 150), 1, PICKUP_SIZE)]
        
        # Add some pickup items 
        #Pickup("Gem", Point(300, 150), 5, pickup_size)
        #Pickup("Life", Point(400, 150), 1, pickup_size)     
        #Pickup("Heart", Point(500, 150), 10, pickup_size)
        #Pickup("Bullet", Point(600, 150), 1, pickup_size)

        # Things that don't collide (no hitbox, only image)
        self._bg_objects = [background_obj(Point(550, 500), ACTOR_WIDTH, ROCK_BLUE), background_obj(Point(0, 150), ACTOR_WIDTH, ROCK_BLACK), background_obj(Point(500, 150), ACTOR_WIDTH, ROCK_BLUE), background_obj(Point(0, 600), ACTOR_WIDTH, ROCK_BLACK), background_obj(Point(800, 750), ACTOR_WIDTH, ROCK_BLUE)]
        
class Hidden_Scene(Scene):
    def __init__(self):
        # Need to initialize the connection dictionary
        super().__init__()
        self._name = "Hidden"

        self._hidden_enemies.append(Enemy("enemy1", Point(200, 200), ACTOR_WIDTH, ACTOR_HEIGHT, AGGRO))

        self._objects = []
        self._objects.append(Pickup(GEM_NAME + str(1), Point(100, 150), 1, PICKUP_SIZE))
        self._objects.append(Pickup(GEM_NAME + str(2), Point(200, 200), 5, PICKUP_SIZE, "BLUE"))
        self._objects.append(Pickup(GEM_NAME + str(3), Point(125, 175), 1, PICKUP_SIZE))
        self._objects.append(Pickup(GEM_NAME + str(4), Point(300, 300), 1, PICKUP_SIZE))
        self._objects.append(Pickup(BOSS_KEY_NAME + str(1), Point(300, 450), 1, PICKUP_SIZE))

class Boss_Scene(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Boss"
        self._enemies = [Boss(BOSS_NAME, Point(300, 150), ACTOR_WIDTH *3,  ACTOR_WIDTH *5, [Point(300, 150), Point(600, 150)])]
