from actors.Fighting_Actor import Fighting_Actor
from point import Point
from director import ACTOR_SIZE

SPIRTE_PATH = "assets\\Alien\\Alien_idle3.png"
#ROUTE_OPTIONS = {"DEFAULT": }

# Square
ROUTE_POINTS = ["ONE", "TWO", "THREE", "FOUR"]
ROUTE_STOPS = {"ONE": Point(100, 300), "TWO": Point(500, 300), "THREE": Point(500, 500), "FOUR": Point(100, 500)}
ROUTE_DIRECTION = {"ONE": [1, 0], "TWO": [0, 1], "THREE": [-1, 0], "FOUR": [0, -1]}

# Player Aggro
"""
move()
If the Player's position within (DETECTION_RANGE)
    then Enemy's velocity --> Player's position
    (figuring out difference in positions and)

Else
    Continue moving on it's path
    Move towards next point
-   -   -   -   -

Enemy --> point
point can be reassinged to the Player's position (aggro)

"""


# TODO: Double check that Collision Actor has all shared code between Enemy and Player
class Enemy(Fighting_Actor):
    def __init__(self, name, position, size, path = "default", image="", color="WHITE"):
        super().__init__(name, position, size, image, color)
        self._frames = ["Alien\\Alien_idle3.png"]
        self._velocity = [-1, 0]
        self._max_HP = 15
        self._current_HP = self._max_HP

        self._route = [Point(100, 300), Point(500, 300), Point(500, 500), Point(100, 500)]
        self._route_item = 0
        self._goal_position = self._route[self._route_item]
    
    def move(self):
        """
            TODO: Implement some kind of algorithm for enemy movement
            Example: Move randomly within a certain range in the Scene
        """
        super().move()
        # GOAL: Move to goal point

        # TODO: Implement this portion, goal based rather than path/route based
        # if self._position == self._goal_position:
        #     # Move to the next position in the route
        #     self._route_item += 1
        #     if self._route_item > len(self._route):
        #         self._route_item = 0
        #     self._goal_position = self._route[self._route_item]

        for point in ROUTE_POINTS:
            if self._position == ROUTE_STOPS[point]:
                self._velocity = ROUTE_DIRECTION[point]