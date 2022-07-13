from actors.Fighting_Actor import Fighting_Actor
from point import Point
from constants import ACTOR_SIZE

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

        self._route = [Point(500, 300), Point(100, 300), Point(100, 500), Point(500, 500)]
        self._route_item = 0
        self._goal_position = self._route[self._route_item]
    
    def get_aggro(self, player_pos):
        # TODO: Is the Player close enough for the enemy to want to move towards the Player?
        # Calculate difference between the Player and self
        # If aggro_distance <= player_distance
        # Then return True, will go after the Player
        # Else return False, will continue on route
        
        pass

    def get_velocity(self):
        """
            The Enemy will move towards it's Goal Position, whether
             that be a set Route or the Player (not yet implemented)
        """
        new_velocity = [0, 0]

        # TODO: Enemies attacking the Player
        # if get_agrro() returns True # If the Player is within detection range
        # Goal position = Player # Goal is to move towards the Player

        # Calculate the difference in position from current Point and Goal Point
        x_diff = int(self._position.get_x() - self._goal_position.get_x())
        y_diff = int(self._position.get_y() - self._goal_position.get_y())
        # 0 - same position
        # - integer/float - goal is to the left/down (velocity: 1)
        # + integer/float - goal is to the right/up (velocity: -1)

        # if there is no difference, then move to new goal position
        # NOTE: For aggro, add OR player_aggro_off~ this would change it's goal_position from the Player's
        if x_diff == 0 and y_diff == 0:
            # Changes goal position to the next route position (looping over the list)
            self._route_item += 1
            if self._route_item >= len(self._route):
                self._route_item = 0
            self._goal_position = self._route[self._route_item]
        else:
            # Prioritize one set of movement, Enemies will have grid movement
            # Otherwise remove if abs... and have both if/else statements one after the other
            if abs(y_diff) > abs(x_diff):
                # Positive or negative difference
                if y_diff > 1:
                    new_velocity[1] = -1
                else:
                    new_velocity[1] = 1
            else:
                # Positive or negative difference
                if x_diff > 1:
                    new_velocity[0] = -1
                else:
                    new_velocity[0] = 1
        # Update the velocity
        self._velocity = new_velocity
        return self._velocity