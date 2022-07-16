from actors.actor import Actor
from actors.enemy import Enemy, Point, ACTOR_SIZE
from actors.Boss import Boss
from actors.hitbox import Hitbox
from actors.background_obj import background_obj, collidable_obj

"""
    Add all the items, Enemies, Boss to the things in a scene
"""
# TODO: Design the scenes, add the rocks/objects and enemies to them
class Scene():
    def __init__(self):

        self._enemies = []
        # Rocks, barriers, barrels
        # Just anything the Player can collide with
        # self._colliders, self._background_objects
        # Object Parameters - Position (Top, Bottom, Left, Right) or XY coordinate for TL/BR, color
        self._objects = [collidable_obj("Wall", 450, 100), ACTOR_SIZE), ]

        self._exit_areas = {"TOP": None, "BOTTOM": None, "LEFT": None, "RIGHT": None}
        self._connections = {"TOP": None, "BOTTOM": None, "LEFT": None, "RIGHT": None}

    def add_connection(self, direction, TL_point, BR_point, scene):
        """
            Add a connection to the current scene given a direction and a scene.
        """
        self._connections[direction] = scene
        self._exit_areas[direction] = Hitbox(TL_point.get_y(), BR_point.get_y(), TL_point.get_x(), BR_point.get_x())

    def get_connection(self, direction):
        """
            Returns the scene that is connected in the given direction.
        """
        return self._connections[direction]

    def get_enemies(self):
        return self._enemies

    def get_objects(self):
        return self._objects

class Scene1(Scene):
    def __init__(self):
        super().__init__()
        self._enemies = [Enemy("Enemy1", Point(100, 100), ACTOR_SIZE), Enemy("Enemy2")]
        self._objects = []

class Boss_Scene(Scene):
    def __init__(self):
        super().__init__()
        self._enemies = [Boss("Boss", Point(), ACTOR_SIZE *2)]
