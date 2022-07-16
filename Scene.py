from turtle import back
from actors.enemy import Enemy, Point, ACTOR_SIZE
from actors.Boss import Boss
from actors.hitbox import Hitbox
from actors.background_obj import background_obj, collidable_obj
from constants import ROCK_BLACK, ROCK_BLACK_LONG, ROCK_BLUE, ROCK_BLUE_LONG, ACTOR_SIZE, WINDOW_MAX_X, WINDOW_MAX_Y
# from constants import *
from actors.pickup import *


"""
    Add all the items, Enemies, Boss to the things in a scene
"""
# TODO: Design the scenes, add the rocks/objects and enemies to them
class Scene():
    def __init__(self):
        self._name = "None"
        self._enemies = []
        # Rocks, barriers, barrels
        # Just anything the Player can collide with
        # self._colliders, self._background_objects
        # Object Parameters - Position (Top, Bottom, Left, Right) or XY coordinate for TL/BR, color
        self._bg_objects = []
        self._objects = []

        self._exit_areas = {"TOP": None, "BOTTOM": None, "LEFT": None, "RIGHT": None}
        self._connections = {"TOP": None, "BOTTOM": None, "LEFT": None, "RIGHT": None}
        # {"TOP": "BOSS"}

    def get_name(self):
        return self._name

    def add_connection(self, direction, scene):
        """
            Add a connection to the current scene given a direction and a scene.
        """
        self._connections[direction] = scene
        #self._exit_areas[direction] = 

    def get_connection(self, direction):
        """
            Returns the scene that is connected in the given direction.
        """
        return self._connections[direction]

    def get_enemies(self):
        return self._enemies

    def get_objects(self):
        return self._objects

    def get_bg_objects(self):
        return self._bg_objects

class Spawn_scene(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Spawn"
        #self._enemies = []
        self._bg_objects = [background_obj(Point(0, 100), ACTOR_SIZE, ROCK_BLACK), background_obj(Point(100, 300), ACTOR_SIZE, ROCK_BLACK_LONG), background_obj(Point(500, 700), ACTOR_SIZE, ROCK_BLUE_LONG)]
        
        #self._objects = [collidable_obj("Wall", Point(450, 100), ACTOR_SIZE)]

class Scene2(Scene):
    def __init__(self):
        super().__init__()
        self._enemies = [Enemy("enemy1", Point(100, 650), ACTOR_SIZE, [Point(100, 650), Point(300, 650)]), Enemy("enemy2", Point(200, 400), ACTOR_SIZE, [Point(400, 400), Point(200, 400)]), Enemy("enemy3", Point(150, 200), ACTOR_SIZE, [Point(350, 200), Point(150, 200)])]

class Scene1(Scene):
    def __init__(self):
        super().__init__()
        self._name = "Scene1"
        self._enemies = [Enemy("Enemy1", Point(100, 100), ACTOR_SIZE), Enemy("Enemy2", Point(400, 400), ACTOR_SIZE)]

        self._objects = [collidable_obj("Wall", Point(450, 100), ACTOR_SIZE)]

class TestScene(Scene):
    def __init__(self):
        super().__init__()
        
        # TODO: All the enemies will be created with the scene, these are for testing
        #       Put all of these test items in a Scene called "TEST"
        pickup_size = ACTOR_SIZE //2

        # Adds
        self._enemies = [Enemy("Enemy1", Point(int(WINDOW_MAX_X * 2/3) - 5, WINDOW_MAX_Y//2), ACTOR_SIZE), Enemy("Enemy2", Point(int(WINDOW_MAX_X * 1/3), WINDOW_MAX_Y//2), ACTOR_SIZE), Enemy("Enemy3", Point(int(WINDOW_MAX_X * 2/3) + 75, WINDOW_MAX_Y//2), ACTOR_SIZE), Enemy("Enemy4", Point(int(WINDOW_MAX_X * 1/3) - 75, WINDOW_MAX_Y//2), ACTOR_SIZE)]
        
        # Adds the pickups
        self._objects = [ReusablePickup("Gem", Point(300, 150), 5, pickup_size), ReusablePickup("Life", Point(400, 150), 1, pickup_size), ReusablePickup("Heart", Point(500, 150), 10, pickup_size), ReusablePickup("Bullet", Point(600, 150), 1, pickup_size)]
        
        # Things that don't collide
        self._bg_objects = [background_obj(Point(550, 500), ACTOR_SIZE, ROCK_BLUE), background_obj(Point(0, 150), ACTOR_SIZE, ROCK_BLACK_LONG), background_obj(Point(500, 150), ACTOR_SIZE, ROCK_BLUE_LONG), background_obj(Point(0, 600), ACTOR_SIZE, ROCK_BLACK_LONG), background_obj(Point(800, 750), ACTOR_SIZE, ROCK_BLUE_LONG)]
        
        # Things that do collide but DON'T move
        self._objects = [collidable_obj("Rock", Point(650, 500), ACTOR_SIZE, ROCK_BLACK)]
        
        #self._scene_manager.add_enemy(Enemy("Enemy5", Point(200a, 200), self._actor_size, [Point(450, 200), Point(550, 200)]))
        
        # Add some pickup items
        #self._scene_manager.add_collider(Pickup("Gem", Point(300, 150), 5, pickup_size))        
        #self._scene_manager.add_collider(Pickup("Life", Point(400, 150), 1, pickup_size))        
        #self._scene_manager.add_collider(Pickup("Heart", Point(500, 150), 10, pickup_size))
        #self._scene_manager.add_collider(Pickup("Bullet", Point(600, 150), 1, pickup_size))
        
        # Infinity hahaha
        
        #self._scene_manager.add_collider(Pickup("Bullet", Point(550, 150), 1, self._actor_size))

class Boss_Scene(Scene):
    def __init__(self):
        super().__init__()
        #self._enemies = [Boss("Boss", Point(), ACTOR_SIZE *2)]
