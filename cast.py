"""
    TODO: Can rename to Scene Manager? Is in charge of making sure the Player
     interacts correctly with all items in the Scene (another new Object - 
     holds list of enemies and how to transition from this scene to another scene?)
"""

class Cast():
    """
        A collection of Actors and Messages to display on the GUI.
    """
    def __init__(self):
        # TODO: Change to have a different list of Enemies/Colliders based on scene
        # Colliders can include things like walls, barrels, etc <-- Another new class or just a Collision Actor with no movement (Collision Actor's Move method is just 'pass' then Enemy and Player would override Move)
        self._players = []
        self._messages = []
        self._buttons = {}
        self._BUTTON_NAMES = ["PLAY_AGAIN", "EXIT"]

    def add_player(self, new_player):
        """
            Adds a new player to the Cast's list of Players.
        """
        self._players.append(new_player)
        self.add_message(new_player.get_score())

    def get_players(self):
        """
            Returns the list of Players.
        """
        return self._players

    def move_players(self):
        """
            Moves the Players.
        """
        for player in self._players:
            player.move()

    def reset_players(self):
        """
            Moves the Players to their spawn points.
        """
        for player in self._players:
            player.respawn()

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
        assert(type == self._BUTTON_NAMES[0] or type == self._BUTTON_NAMES[1])
        self._buttons[type] = new_button

    def get_buttons(self):
        """
            Returns a list of buttons if they've been added.
        """
        button_list = []
        if len(self._buttons) > 0:
            button_list = [self._buttons[self._BUTTON_NAMES[0]], self._buttons[self._BUTTON_NAMES[1]]]
        return button_list

    def check_replay_buttons(self, cursor_position):
        """
            Returns if the user has chosen to Play Again (True) or Exit (False).
        """
        print(f"Cursor click at [{cursor_position.get_x()}, {cursor_position.get_y()}]")
        # If the Play Again button has been clicked.
        if self._buttons[self._BUTTON_NAMES[0]].pressed(cursor_position):
            return True
        # Else if the Exit button has been clicked.
        elif self._buttons[self._BUTTON_NAMES[1]].pressed(cursor_position):
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