from collisionHandler import Collision_Handler
from constants import *
from actors.exit import Exit
from point import Point
import copy

# Scene bounds (all the same)
scene_edges = {"TOP": UI_Y_POS, "BOTTOM": WINDOW_MAX_Y, "LEFT": 0, "RIGHT": WINDOW_MAX_X}

# WALL["TOP"], WALL["LEFT"] ...
EXITS = {"TOP": Exit("TOP", Point((scene_edges["RIGHT"] - scene_edges["LEFT"])//2, scene_edges["TOP"]), scene_edges["TOP"], scene_edges["TOP"], scene_edges["LEFT"], scene_edges["RIGHT"]), "LEFT": Exit("LEFT", Point(scene_edges["LEFT"], (scene_edges["BOTTOM"] - scene_edges["TOP"])//2), scene_edges["TOP"], scene_edges["BOTTOM"], scene_edges["LEFT"], scene_edges["LEFT"]), "RIGHT": Exit("RIGHT", Point(scene_edges["RIGHT"], (scene_edges["BOTTOM"] - scene_edges["TOP"])//2), scene_edges["TOP"], scene_edges["BOTTOM"], scene_edges["RIGHT"], scene_edges["RIGHT"]), "BOTTOM": Exit("BOTTOM", Point((scene_edges["RIGHT"] - scene_edges["LEFT"])//2, scene_edges["BOTTOM"]), scene_edges["BOTTOM"], scene_edges["BOTTOM"], scene_edges["LEFT"], scene_edges["RIGHT"])}

class Scene_Manager():
    """
       An object that is in charge of making sure all objects in the current scene interact properly 
    """
    def __init__(self, max_x, max_y):
        # TODO: remove max_x, max_y - temporary EXIT sensing
        self._max_x = max_x
        self._max_y = max_y
        
        # Could make player it's own object to simplify the reset of colliding actors, enemies, and object lists?
        #self._player = None
        self._HUD = []

        self._player_entrance = None

        # Colliders can include things like rocks/walls, barrels, etc <-- Another new class or just a Collision Actor with no movement (Collision Actor's Move method is just 'pass' then Enemy and Player would override Move)
        self._colliding_actors = []

        # These items are added to the colliding actors list, but have their own lists for specific functions
        self._enemies = []
        self._objects = []

        # Background objects, without colliders
        self._images = []

        # Currently only being used for Game Over
        self._messages = []
        self._REPLAY_BUTTON_NAMES = ["PLAY_AGAIN", "EXIT"]        
        # If there are more buttons, add to the list? Not very maintainable here..
        # Maybe have differnt lists of buttons? (self._replay_buttons, and self._UI_buttons?)
        self._buttons = {}
        
        # Scene Loading
        self._scene_loaded = False
        self._exits = EXITS

        # NOTE: These items could be in the Scene object, but then the Scene Manager goes
        #       self._current_scene.exit("TOP") --> returned a new Scene to load (or False if no connection there)
        # The Scenes connected to the current scene        
        self._scene_connections = {"TOP": None, "LEFT": None, "RIGHT": None, "BOTTOM": None}
        # The Hitbox areas the Player needs to step in to leave the scene in the specified direction
        self._exit_areas = {"TOP": None, "LEFT": None, "RIGHT": None, "BOTTOM": None}

        self._collision_handler = Collision_Handler()

    def add_player(self, new_player):
        """
            Adds a new Player to the Cast's list of Colliders.
            Will always be the first collider (index = 0)
            Makes sure to add the score/UI as well
        """
        self.add_collider(new_player)
        player_HUD = new_player.get_HUD()
        for counter in player_HUD:
            self.add_HUD(counter)

    def add_HUD(self, HUD_item):
        """
            Adds a new Counter to the HUD
        """
        self._HUD.append(HUD_item)

    def get_HUD(self):
        """
            Returns the HUD items
        """
        return self._HUD

    def reset(self):
        """
            Reset all the knowledge that the Scene Manager has
            Except for the Player and the HUD
        """
        player = copy.copy(self._colliding_actors[0])
        # NOTE: not sure if delete does anything in python?
        del self._colliding_actors
        self._colliding_actors = []
        
        self._colliding_actors.append(player)
        
        if not (self._player_entrance == None):
            # Move player to the entrance
            self._colliding_actors[0].enter_scene(Point(450, 300))

        for direction in DIRECTIONS:
            self._colliding_actors.append(self._exits[direction])
        
        del self._enemies
        self._enemies = []
        del self._objects
        self._objects = []
        del self._images
        self._images = []

    def setup_scene(self, scene):
        self.reset()
        self._current_scene = scene

        for direction in DIRECTIONS:
            self._scene_connections[direction] = self._current_scene.get_connection(direction)

        new_enemies = self._current_scene.get_enemies()
        new_objects = self._current_scene.get_objects()
        new_bg_objects = self._current_scene.get_bg_objects()

        for enemy in new_enemies:
            self.add_enemy(enemy)
        
        for object in new_objects:
            self.add_collider(object)

        for bg_object in new_bg_objects:
            self.add_image(bg_object)

        # NOTE: Move this to a place after scene connections, enemies, etc are loaded
        self._scene_loaded = True

    def add_image(self, actor):
        """
            Adds an actor that has only position and image arguements
        """
        self._images.append(actor)

    def get_exits(self):
        return self._exits

    #def load_scene(scene)
        # Add all the Scene's colliders to self._colliders
    
    #def exit_scene()
        # removes all the colliders from the other scene (self._collider = just the player)

    def add_enemy(self, enemy):
        """
            Adds a new enemy to the loaded Scene.
        """
        self._enemies.append(enemy)
        self.add_collider(enemy)

    def add_collider(self, new_collider):
        """
            Adds a new Collider to the Cast's list of Colliders
        """
        self._colliding_actors.append(new_collider)

    def get_colliders(self):
        """
            Returns the list of Colliders. For detecting collisions.
        """
        return self._colliding_actors

    def get_objects(self):
        return self._objects

    def get_bg_objects(self):
        return self._images

    def continue_game(self):
        """
            Moves all Colliders and checks their status (is_alive).
            (non-moving will have "pass" in their move method)
        """
        # Move each colliding actor, but only if it is alive
        for collider in self._colliding_actors:
            # If it is not alive
            if not collider.is_alive():
                if not collider.get_name() == PLAYER_NAME:
                    # Remove the actor if it is not the Player
                    self._colliding_actors.remove(collider)
                else:
                    # The Player has died, and the game is over
                    return False
            collider.move()
        
        # Then check for actions, and collision
        self.check_actions()
        
        # Return if the game should continue
        return True

    def reset_player(self):
        """
            Moves the Player to their spawn point.
        """
        self._colliding_actors[0].respawn()

    def check_actions(self):
        """
            Checks Player and Enemy Actions other than movement
        """
        # Checks if the Player has shot a bullet
        new_bullet = self._colliding_actors[0].check_shoot()
        # If there is a bullet to shoot
        if not (bool(new_bullet) == False):
            self._colliding_actors.append(new_bullet)

        # Check if the enemies should aggro onto the Player
        for enemy in self._enemies:
            # Check if the Player is close enough to attack
            enemy.get_aggro(self._colliding_actors[0].get_point_position())

    def check_collisions(self):
        """
            More like Check_exit, sees if the Player is trying to leave (by colliding with a wall/exit)
            Checks if there has been a collision between any of the colliders.
        """
        if len(self._colliding_actors) > 1:
            # Only check for collisions if there are other colliding Actors
            exit_direction = self._collision_handler.check_exit(self._colliding_actors)
            if not(exit_direction == None):
                print(f"Player is trying to exit {exit_direction} to {self._scene_connections[exit_direction]}")
                self._player_entrance = self.get_opposite_direction(exit_direction)
                return self._scene_connections[exit_direction]
        # If there is no exiting
        return None

    def get_opposite_direction(self, direction):
        if direction == "TOP":
            return "BOTTOM"
        if direction == "BOTTOM":
            return "TOP"
        if direction == "RIGHT":
            return "LEFT"
        if direction == "LEFT":
            return "RIGHT"

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