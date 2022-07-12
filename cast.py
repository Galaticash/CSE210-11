from collisionHandler import Collision_Handler
from actors.wall import Wall

"""
    TODO: Is in charge of making sure the Player
     interacts correctly with all items in the Scene (another new Object - 
     holds list of enemies and how to transition from this scene to another scene?)
"""

class Scene_Manager():
    """
        A collection of Actors and Messages to display on the GUI.
    """
    def __init__(self, max_x, max_y):
        # TODO: remove max_x, max_y - temporary wall sensing
        self._max_x = max_x
        self._max_y = max_y
        # TODO: Change to have a different list of Enemies/Colliders based on scene
        # Colliders can include things like walls, barrels, etc <-- Another new class or just a Collision Actor with no movement (Collision Actor's Move method is just 'pass' then Enemy and Player would override Move)
        self._colliders = []
        self._messages = []
        self._REPLAY_BUTTON_NAMES = ["PLAY_AGAIN", "EXIT"]
        self._walls = {"TOP": None, "LEFT": None, "RIGHT": None, "BOTTOM": None}
        self._scene_connections = {"TOP": None, "LEFT": None, "RIGHT": None, "BOTTOM": None}
        # If there are more buttons, add to the list? Not very maintainable here..
        # Maybe have differnt lists of buttons? (self._replay_buttons, and self._UI_buttons?)
        self._buttons = {}

        self._collision_handler = Collision_Handler()
        self.add_walls()

    def add_player(self, new_player):
        """
            Adds a new Player to the Cast's list of Colliders.
            Will always be the first collider (index = 0)
            Makes sure to add the score/UI as well
        """
        self.add_collider(new_player)
        self.add_message(new_player.get_score())

    def add_walls(self):
        # TODO: Given a scene, finds wall edges
        # TODO: Fix to fit Constant DIRECTIONS
        self._walls["TOP"] = Wall(self._max_x, self._max_y, 0, 0, 0, self._max_x)
        self._walls["LEFT"] = Wall(self._max_x, self._max_y, 0, self._max_y, 0, 0)
        self._walls["RIGHT"] = Wall(self._max_x, self._max_y, 0, self._max_y, self._max_x, self._max_x)
        self._walls["BOTTOM"] = Wall(self._max_x, self._max_y, self._max_y, self._max_y, 0, self._max_x)

    def get_walls(self):
        return self._walls

    #def load_scene(scene)
        # Add all the Scene's colliders to self._colliders
    
    #def exit_scene()
        # removes all the colliders from the other scene (self._collider = just the player)

    #def add_scene_border(self):

    def add_collider(self, new_collider):
        """
            Adds a new Collider to the Cast's list of Colliders
        """
        self._colliders.append(new_collider)

    def get_colliders(self):
        """
            Returns the list of Colliders.
        """
        return self._colliders

    def move_colliders(self):
        """
            Moves all moving Colliders.
            Any non-moving will have "pass" in their move method
        """
        for collider in self._colliders:
            collider.move()

    def reset_player(self):
        """
            Moves the Player to their spawn point.
        """
        self._colliders[0].respawn()

    def check_collisions(self):
        """
            Checks if there has been a collision between any of the colliders.
        """
        self._collision_handler.check_exit(self._colliders[0], self._walls)
        self._collision_handler.check(self._colliders)

    def add_message(self, new_message):
        """
            Adds a new message to the Cast's list of Messages.
        """
        self._messages.append(new_message)

    def get_messages(self):
        """
            Returns the list of Messages.
        """
        return self._messages

    def remove_game_over(self):
        """
            Removes the Game Over Message.
        """
        self._messages.pop()

    def add_button(self, type, new_button):
        """
            Adds a new button to the Cast.
        """
        # Checks that the new_button is either "PLAY AGAIN" or "EXIT"
        assert(type == self._REPLAY_BUTTON_NAMES[0] or type == self._REPLAY_BUTTON_NAMES[1])
        self._buttons[type] = new_button

    def get_buttons(self):
        """
            Returns a list of buttons if they've been added.
        """
        button_list = []
        if len(self._buttons) > 0:
            button_list = [self._buttons[self._REPLAY_BUTTON_NAMES[0]], self._buttons[self._REPLAY_BUTTON_NAMES[1]]]
        return button_list

    def check_replay_buttons(self, cursor_position):
        """
            Returns if the user has chosen to Play Again (True) or Exit (False).
        """
        print(f"Cursor click at [{cursor_position.get_x()}, {cursor_position.get_y()}]")
        # If the Play Again button has been clicked.
        if self._buttons[self._REPLAY_BUTTON_NAMES[0]].pressed(cursor_position):
            return True
        # Else if the Exit button has been clicked.
        elif self._buttons[self._REPLAY_BUTTON_NAMES[1]].pressed(cursor_position):
            return False
        # The user clicked elsewhere on the screen.
        else:
            # No choice was made.
            return None

    def remove_buttons(self):
        """
            Removes the buttons from the Cast.
        """
        del self._buttons
        self._buttons = {}