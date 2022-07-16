from actors.collision_actor import *
from actors.Fighting_Actor import Fighting_Actor

SPIRTE_PATH = "Alien\\Alien_idle3.png"

# TODO: Move these comments to notes
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

"""
class Route():
    def __init__(self):
        self._path = [Point(500, 300), Point(100, 300), Point(100, 500), Point(500, 500)]

"""

class Enemy(Fighting_Actor):
    def __init__(self, name, position, size, path = [Point(500, 300), Point(100, 300), Point(100, 500), Point(500, 500)], image="blank.png", color="WHITE"):
        # Above, when creating Enemy, pass in a path (list of Points [Point(1, 2)])
        super().__init__(name, position, size, image, color)
        self._frames = ["Alien\\Alien_idle3.png", "Alien\\Alien_run1.png", "Alien\\Alien_run2.png", "Alien\\Alien_run3.png", "Alien\\Alien_run4.png", "Alien\\Alien_run5.png", "Alien\\Alien_run6.png"]
        self._velocity = [-1, 0]
        self._max_HP = 15
        self._current_HP = self._max_HP

        self._aggro = False
        self._player_position = Point(0, 0)

        # Change Path/Route here
        self._route = path
        
        self._route_item = 0
        self._goal_position = self._route[self._route_item]

        enemy1 = Enemy(enemy1, Point(100, 650), ACTOR_SIZE, [Point(100, 650), Point(300, 650)])
        enemy2 = Enemy(enemy2, Point(200, 400), ACTOR_SIZE, [Point(400, 400), Point(200, 400)])
        enemy3 = Enemy(enemy3, Point(150, 200), ACTOR_SIZE, [Point(350, 200), Point(150, 200)])

    
    def get_aggro(self, player_pos):
        # TODO: Is the Player close enough for the enemy to want to move towards the Player?
        # Calculate difference between the Player and self
        # If aggro_distance <= player_distance
        # Then return True, will go after the Player
        # Else return False, will continue on route
        self._player_position = player_pos
        #self._aggro = True

    def get_velocity(self):
        """
            The Enemy will move towards it's Goal Position, whether
             that be a set Route or the Player (not yet implemented)
        """
        if self._movement_control:
            new_velocity = [0, 0]

            # TODO: Enemies attacking the Player
            if self._aggro: # If the Player is within detection range
                self._goal_position = self._player_position
            else:
                # If the player is no longer in bounds
                pass
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
        else:
            self.override_update()
        return super().get_velocity()

    def is_hit(self, other_collider):
        """
            Other enemies do not hurt eachother
        """
        if not (isinstance(other_collider, Enemy)):
            return super().is_hit(other_collider)
        else:
            return False