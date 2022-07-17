from actors.collision_actor import *
from actors.Fighting_Actor import Fighting_Actor

SPIRTE_PATH = "Alien\\Alien_idle3.png"

# Idea: Add gem pickup spawning after defeat (similar to Bullet creation)

class Enemy(Fighting_Actor):
    """
        An Actor that the Player can fight against and defeat.
        It will follow a given path, and can aggro onto the Player.
    """
    def __init__(self, name, position, size, path = [Point(500, 300), Point(100, 300), Point(100, 500), Point(500, 500)], image="blank.png", color="WHITE"):
        super().__init__(name, position, size, image, color)
        # Animation
        self._frames = ["Alien\\Alien_idle3.png", "Alien\\Alien_run1.png", "Alien\\Alien_run2.png", "Alien\\Alien_run3.png", "Alien\\Alien_run4.png", "Alien\\Alien_run5.png", "Alien\\Alien_run6.png"]
        
        # HP setup
        self._max_HP = 15
        self._current_HP = self._max_HP

        # Aggro logic
        self._aggro = False
        self._agrro_distance = 0
        self._player_position = Point(0, 0)

        # Movement logic, starts by travelling to the first point on it's route
        self._route = path        
        self._route_item = 0
        self._goal_position = self._route[self._route_item]

    def set_aggro(self, bool):
        """
            Change the agrro values
        """
        self._aggro = bool

    def get_aggro(self, player_pos):
        """
            Updates the Player's position and calculates if the
             Player is close enough for the enemy to aggro onto them.
        """        
        self._player_position = player_pos
        # TODO: Calculate difference between the Player and self
        # x_dif = abs(self._position.get_x() - player_pos.get_x())
        # y_dif = abs(self._position.get_y() - player_pos.get_y())
        # if self._agrro_distance <= (x_dif + y_dif) or sqrt(x_dif^2 + y_dif^2) <- Pythagorian?
        # Then return self._aggro = True, will go after the Player
        # Else return False, will continue on route
        
        # DEBUG: Test aggro
        #self._aggro = True
        pass # to help shrink the method in VS Code

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
        # Literally return self._velocity
        return super().get_velocity()

    def is_hit(self, other_collider):
        """
            Other enemies do not hurt eachother
        """
        if not (isinstance(other_collider, Enemy)):
            return super().is_hit(other_collider)
        else:
            return False