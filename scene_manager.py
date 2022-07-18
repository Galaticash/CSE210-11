from collisionHandler import Collision_Handler
from actors.background_obj import collidable_obj
from constants import *
from actors.exit import Exit
from point import Point
import copy

# Scene bounds (all the same)
scene_edges = {"TOP": UI_Y_POS, "BOTTOM": WINDOW_MAX_Y, "LEFT": 0, "RIGHT": WINDOW_MAX_X}
EXIT_POSITIONS = {"TOP": Point((scene_edges["RIGHT"] - scene_edges["LEFT"])//2, scene_edges["TOP"]), "BOTTOM": Point((scene_edges["RIGHT"] - scene_edges["LEFT"])//2, scene_edges["BOTTOM"]), "LEFT": Point(scene_edges["LEFT"], (scene_edges["BOTTOM"] - scene_edges["TOP"])//2 +  scene_edges["TOP"]), "RIGHT": Point(scene_edges["RIGHT"], (scene_edges["BOTTOM"] - scene_edges["TOP"])//2 + scene_edges["TOP"])}
# scene_edges["TOP"], scene_edges["TOP"], scene_edges["LEFT"], scene_edges["RIGHT"]
WALL_WIDTH = {"TOP": scene_edges["RIGHT"] - scene_edges["LEFT"], "BOTTOM": scene_edges["RIGHT"] - scene_edges["LEFT"], "LEFT": 0, "RIGHT": 0}
WALL_HEIGHT = {"TOP": 0, "BOTTOM": 0, "LEFT": scene_edges["BOTTOM"] - scene_edges["TOP"], "RIGHT": scene_edges["BOTTOM"] - scene_edges["TOP"]}

# The exits that, when collided with, move the Player to the next scene
EXITS =  {"TOP": Exit("TOP", EXIT_POSITIONS["TOP"], WALL_WIDTH["TOP"], WALL_HEIGHT["TOP"]), "LEFT": Exit("LEFT", EXIT_POSITIONS["LEFT"], WALL_WIDTH["LEFT"], WALL_HEIGHT["LEFT"]), "RIGHT": Exit("RIGHT", EXIT_POSITIONS["RIGHT"], WALL_WIDTH["RIGHT"], WALL_HEIGHT["RIGHT"]), "BOTTOM": Exit("BOTTOM", EXIT_POSITIONS["BOTTOM"], WALL_WIDTH["BOTTOM"], WALL_HEIGHT["BOTTOM"])}

# Blockers are placed if there is no connection
EXIT_BLOCKERS = {"TOP": collidable_obj("TOP_WALL", EXIT_POSITIONS["TOP"], WALL_WIDTH["TOP"], WALL_HEIGHT["TOP"]), "BOTTOM": collidable_obj("BOTTOM_WALL", EXIT_POSITIONS["BOTTOM"], WALL_WIDTH["BOTTOM"], WALL_HEIGHT["BOTTOM"]), "LEFT": collidable_obj("LEFT_WALL", EXIT_POSITIONS["LEFT"], WALL_WIDTH["LEFT"], WALL_HEIGHT["LEFT"]), "RIGHT": collidable_obj("RIGHT_WALL", EXIT_POSITIONS["RIGHT"], WALL_WIDTH["RIGHT"], WALL_HEIGHT["RIGHT"])}

# Where the Player enters the scene
ENTRANCE_PADDING = ACTOR_WIDTH + 25
ENTRANCE_POINTS = {"TOP": Point(EXIT_POSITIONS["TOP"].get_x(), EXIT_POSITIONS["TOP"].get_y() + ENTRANCE_PADDING),"BOTTOM": Point(EXIT_POSITIONS["BOTTOM"].get_x(), EXIT_POSITIONS["BOTTOM"].get_y() - ENTRANCE_PADDING), "LEFT": Point(EXIT_POSITIONS["LEFT"].get_x() + ENTRANCE_PADDING, EXIT_POSITIONS["LEFT"].get_y()), "RIGHT": Point(EXIT_POSITIONS["RIGHT"].get_x() - ENTRANCE_PADDING, EXIT_POSITIONS["RIGHT"].get_y())}

#{"TOP": Exit(), "BOTTOM": Exit(), "LEFT": Exit(), "RIGHT": Exit()}

class Scene_Manager():
    """
       An object that is in charge of making sure all Actors in the current scene interact properly. 
    """
    def __init__(self, max_x, max_y):        
        # Could make player it's own object to simplify the reset of colliding actors, enemies, and object lists?
        #self._player = None
        self._HUD = []

        # Player enters from nowhere, spawns in Spawn Scene
        self._player_entrance = None

        # Colliders can include things like rocks/walls, barrels, etc <-- Another new class or just a Collision Actor with no movement (Collision Actor's Move method is just 'pass' then Enemy and Player would override Move)
        self._colliding_actors = []

        # These items are added to the colliding actors list, but have their own lists for specific functions
        self._enemies = []
        self._objects = []

        # Background objects, without colliders
        self._bg_objects = []
        self._foreground_objects = []

        # Currently only being used for Game Over
        # If there are more buttons, add to the list? Not very maintainable here..
        # Maybe have differnt lists of buttons? (self._replay_buttons, and self._UI_buttons?)
        self._messages = []
        self._REPLAY_BUTTON_NAMES = ["PLAY_AGAIN", "EXIT"] # For iterating through the dictionary
        self._buttons = {}  
        
        # Scene Loading
        self._scene_loaded = False
        self._exits = EXITS

        # NOTE: These items could be in the Scene object, but then the Scene Manager goes
        #       self._current_scene.exit("TOP") --> returned a new Scene to load (or False if no connection there)
        # The Scenes connected to the current scene        
        self._scene_connections = {"TOP": None, "LEFT": None, "RIGHT": None, "BOTTOM": None}

        self._collision_handler = Collision_Handler()

## ADDERS AND GETTERS ##

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

    def get_player(self):
        """
            Returns the Player (first colliding Actor)
        """
        return self._colliding_actors[0]

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

    def add_enemy(self, enemy):
        """
            Adds a new enemy to the loaded Scene.
        """
        self._enemies.append(enemy)
        self.add_collider(enemy)

    def get_objects(self):
        return self._objects

    def add_bg_obj(self, actor):
        """
            Adds an Actor to the background (non-colliding).
        """
        self._bg_objects.append(actor)

    def get_bg_objects(self):
        return self._bg_objects

    def add_foreground_obj(self, actor):
        """
            Adds an Actor to the foreground (non-colliding).
        """
        self._foreground_objects.append(actor)

    def get_foreground_objects(self):
        return self._foreground_objects

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

    def get_exits(self):
        """
            DEBUG: Returns the exits so they can be printed
        """
        return self._exits

## OTHER METHODS ##
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
                #print(f"Player is trying to exit {exit_direction} to {self._scene_connections[exit_direction]}")
                self._player_entrance = self.get_opposite_direction(exit_direction)
                return self._scene_connections[exit_direction]
            else:
                self._player_entrance = None
        # If there is no exiting
        return None

    def get_opposite_direction(self, direction):
        """
            Gets the opposite direction, for figuring out
             where the Player will enter the Next Scene.
        """
        if direction == "TOP":
            return "BOTTOM"
        elif direction == "BOTTOM":
            return "TOP"
        elif direction == "RIGHT":
            return "LEFT"
        elif direction == "LEFT":
            return "RIGHT"
        else:
            return None

    def setup_scene(self, scene):
        # Shouldn't be an issue, since all of this has to happen before the next GUI check
        self._scene_loaded = False
        #print(f"Player will enter {scene.get_name()} from {self._player_entrance}")
        self.reset()
        # Move to the next scene
        self._current_scene = scene

        # For every direction,
        for direction in DIRECTIONS:
            # Get the connections for the new scene
            self._scene_connections[direction] = self._current_scene.get_connection(direction)
            # If there isn't a connection, put a blocker instead
            if self._scene_connections[direction] == None:
                self._colliding_actors.append(EXIT_BLOCKERS[direction])
            else:                
                self._colliding_actors.append(self._exits[direction])

        # Put the Player where they entered in,
        if (self._player_entrance == None):
            # UNLESS the game just started, begins at the Spaceship
            self._colliding_actors[0].set_position(Point(450, 300))
        else:
            self._colliding_actors[0].set_position(copy.copy(ENTRANCE_POINTS[self._player_entrance]))

        # Get all the objecs from the new Scene
        new_enemies = self._current_scene.get_enemies()
        new_objects = self._current_scene.get_objects()
        new_bg_objects = self._current_scene.get_bg_objects()
        new_fore_objects = self._current_scene.get_fore_objects()

        # Make sure dead objects aren't added 
        #  (Actors remember if they have already been defeated)
        for enemy in new_enemies:
            if enemy.is_alive():
                self.add_enemy(enemy)
        for object in new_objects:
            if object.is_alive():
                self.add_collider(object)

        # Add bg_objects (spaceship, etc)
        for bg_object in new_bg_objects:
            self.add_bg_obj(bg_object)

        # Add foreground objects (overhanging rocks, etc)
        for fore_object in new_fore_objects:
            self.add_foreground_obj(fore_object)

        self._scene_loaded = True

    def check_replay_buttons(self, cursor_position):
        """
            Returns if the user has chosen to Play Again (True) or Exit (False).
        """
        #print(f"Cursor clicked at [{cursor_position.get_x()}, {cursor_position.get_y()}]")
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

    def remove_game_over(self):
        """
            Removes the Game Over Message.
        """
        self._messages.pop()
        self.remove_buttons()

    def remove_buttons(self):
        """
            Removes the buttons from the Cast.
        """
        del self._buttons
        self._buttons = {}

    def reset(self):
        """
            Reset all the knowledge that the Scene Manager has
            Except for the Player and the HUD
        """
        self._current_scene = None
        
        # Clear the connections dictionary
        del self._scene_connections
        self._scene_connections = {}

        player = copy.copy(self._colliding_actors[0])
        
        # NOTE: not sure if del/delete does anything in python?
        # Delete the colliders list, and restart with only the Player
        del self._colliding_actors
        self._colliding_actors = []
        self._colliding_actors.append(player)

        # Delete every other list, except HUD
        del self._enemies
        self._enemies = []
        del self._objects
        self._objects = []
        del self._bg_objects
        self._bg_objects = []
        del self._foreground_objects
        self._foreground_objects = []