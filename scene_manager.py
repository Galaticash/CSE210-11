from actors.pickup import Pickup
from collisionHandler import Collision_Handler
from sound import Sound
from constants import *
import copy

## Scene Manager Constants ##
from actors.background_obj import collidable_obj
from actors.exit import Exit
# Scene bounds (all the same)
SCENE_EDGES = {"TOP": UI_Y_POS, "BOTTOM": WINDOW_MAX_Y, "LEFT": 0, "RIGHT": WINDOW_MAX_X}
# NOTE: Some funky math for the left/right edges, it goes wrong somewhere, but I was able to adjust it here (//2)
EXIT_POSITIONS = {"TOP": Point((SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"])//2, SCENE_EDGES["TOP"]), "BOTTOM": Point((SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"])//2, SCENE_EDGES["BOTTOM"]), "LEFT": Point(SCENE_EDGES["LEFT"], (SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"])//2 +  SCENE_EDGES["TOP"]), "RIGHT": Point(SCENE_EDGES["RIGHT"], (SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"])//2 + SCENE_EDGES["TOP"])}

# The widths and heights for each Exit/Edge
WALL_WIDTH = {"TOP": SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"], "BOTTOM": SCENE_EDGES["RIGHT"] - SCENE_EDGES["LEFT"], "LEFT": 0, "RIGHT": 0}
WALL_HEIGHT = {"TOP": 0, "BOTTOM": 0, "LEFT": SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"], "RIGHT": SCENE_EDGES["BOTTOM"] - SCENE_EDGES["TOP"]}

# The exits that, when collided with, move the Player to the next scene
EXITS =  {"TOP": Exit("TOP", EXIT_POSITIONS["TOP"], WALL_WIDTH["TOP"], WALL_HEIGHT["TOP"]), "LEFT": Exit("LEFT", EXIT_POSITIONS["LEFT"], WALL_WIDTH["LEFT"], WALL_HEIGHT["LEFT"]), "RIGHT": Exit("RIGHT", EXIT_POSITIONS["RIGHT"], WALL_WIDTH["RIGHT"], WALL_HEIGHT["RIGHT"]), "BOTTOM": Exit("BOTTOM", EXIT_POSITIONS["BOTTOM"], WALL_WIDTH["BOTTOM"], WALL_HEIGHT["BOTTOM"])}

# Blockers are placed if there is no connection (so they can't walk off the screen)
EXIT_BLOCKERS = {"TOP": collidable_obj("TOP_WALL", EXIT_POSITIONS["TOP"], WALL_WIDTH["TOP"], WALL_HEIGHT["TOP"]), "BOTTOM": collidable_obj("BOTTOM_WALL", EXIT_POSITIONS["BOTTOM"], WALL_WIDTH["BOTTOM"], WALL_HEIGHT["BOTTOM"]), "LEFT": collidable_obj("LEFT_WALL", EXIT_POSITIONS["LEFT"], WALL_WIDTH["LEFT"], WALL_HEIGHT["LEFT"]), "RIGHT": collidable_obj("RIGHT_WALL", EXIT_POSITIONS["RIGHT"], WALL_WIDTH["RIGHT"], WALL_HEIGHT["RIGHT"])}

# Where the Player enters the next Scene
ENTRANCE_PADDING = ACTOR_WIDTH + 25
ENTRANCE_POINTS = {"TOP": Point(EXIT_POSITIONS["TOP"].get_x(), EXIT_POSITIONS["TOP"].get_y() + ENTRANCE_PADDING),"BOTTOM": Point(EXIT_POSITIONS["BOTTOM"].get_x(), EXIT_POSITIONS["BOTTOM"].get_y() - ENTRANCE_PADDING), "LEFT": Point(EXIT_POSITIONS["LEFT"].get_x() + ENTRANCE_PADDING, EXIT_POSITIONS["LEFT"].get_y()), "RIGHT": Point(EXIT_POSITIONS["RIGHT"].get_x() - ENTRANCE_PADDING, EXIT_POSITIONS["RIGHT"].get_y())}


class Scene_Manager():
    """
       An object that is in charge of making sure all Actors in the current scene interact properly. 
    """
    def __init__(self, audio_service):  
        # Could skip this line, and just hand it directly to the collision handler,
        # However! Could use it here to play a sound when changing scenes/entering boss scene
        # Hmm, so here it would handle music changes instead of short sound bits
        self._audio_service = audio_service    
        self._music = Sound("crab_rave.mp3")
        self._boss_music = Sound("WindowsXPErrorRemix.mp3")
        self._game_over_sound = Sound("over.wav")
        self._game_start_sound = Sound("start.wav")
        self._current_music = copy.copy(self._music)

        # Could make player it's own object to simplify the reset of colliding actors, enemies, and object lists?
        #self._player = None
        self._HUD = []
        self._win = False

        self._added_number = 0

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
        self._current_scene = None
        self._scene_loaded = False
        self._exits = EXITS

        # NOTE: These items could be in the Scene object, but then the Scene Manager goes
        #       self._current_scene.exit("TOP") --> returned a new Scene to load (or False if no connection there)
        # The Scenes connected to the current scene        
        self._scene_connections = {"TOP": None, "LEFT": None, "RIGHT": None, "BOTTOM": None}

        self._collision_handler = Collision_Handler(self._audio_service)


## MUSIC HANDLING ##
    def music_loop(self):
        """
            Very lazy rn, but I just want to play Crab Rave
        """
        # If no sounds are playing (the music has ended)
        #if self._audio_service.is_sound_playing(self._music) < 1 and self._colliding_actors[0].has_key():
        #    self._audio_service.play_sound(self._music)
        if (not self._audio_service.is_sound_playing(self._current_music)):
            self._audio_service.play_sound(self._current_music)

    def play_sound(self, sound):
        """ 
            Stops the current music to play a sound
        """         
        self.stop_music()
        self._audio_service.play_sound(sound)

    def stop_music(self):
        """
            Stops the current music, could change to pause as well, but eh
        """
        self._audio_service.stop_sound(self._current_music)

    def change_music(self, music):
        """
            Stops the current music, and changes to a new one.
        """
        self.stop_music()
        self._current_music = copy.copy(music)

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
        # Check if the music is still playing, keep it looping   
        self.music_loop()

        # Move each colliding actor, but only if it is alive
        for collider in self._colliding_actors:
            # If it is not alive
            if not collider.is_alive():
                if not collider.get_name() == PLAYER_NAME:
                    # Remove the actor if it is not the Player
                    self._colliding_actors.remove(collider)
                    #print(f"{collider.get_name()} has died!")
                    if collider.get_name() == BOSS_NAME:
                        # If the Boss has been defeated, the Player won the game
                        self._win = True
                        # Probably have it be victory music, and game over
                        self.play_sound(self._game_start_sound)
                        return False
                    if collider.get_name() == BOSS_KEY_NAME + str(1) + "_p":
                        hidden_enemies = self._current_scene.get_hidden_enemies()
                        if len(hidden_enemies) > 0:
                            for enemy in hidden_enemies:
                                self.add_enemy(enemy)
                    # "Enemy1" --> "Enemy"
                    # if len(collider.get_name()) >= len(ENEMY_NAME) and collider.get_name()[:-1] == ENEMY_NAME:
                    #     print("Drop")
                    #     self._objects.append(Pickup(BULLET_NAME + str(self._added_number), collider.get_point_position(), 1))
                    #     self._added_number += 1
                    #     if self._added_number > 9:
                    #         self._added_number = 0
                else:
                    # The Player has died, and the game is over
                    self._win = False
                    self.play_sound(self._game_over_sound)
                    return False
            collider.move()
        
        # Then check for actions, and collision
        self.check_actions()
        
        # Return if the game should continue
        return True

    def restart_game(self, spawn_scene):
        """
            Restarts the game
        """
        self._current_scene = None
        self.reset() # Reset the Scene Manager's knowledge
        self.change_music(self._music)
        self._colliding_actors[0].start_stats() # Resets the Player
        self.setup_scene(spawn_scene) # setup the Spawn Scene

        # Removes game_over cast members (Game Over menu)
        self.remove_game_over()

    def fling_player(self):
        # Flings the Player backwards
        self._collision_handler.fling_object(self._colliding_actors[0])

    def boss_defeated(self):
        return self._win

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
        
        # Go back to normal music if the Player exits the Boss level LOL
        if (not self._current_scene == None):
            # Exiting FROM the Boss Scene
            if self._current_scene.get_name() == "Boss":
                self.change_music(self._music)
        # Coming from Scene None (aka game start)
        else:
            self.play_sound(self._game_start_sound)

        #print(f"Player will enter {scene.get_name()} from {self._player_entrance}")
        self.reset()

        # Move to the next scene
        self._current_scene = scene
        
        # If ENTERING the Boss Scene, and the Boss hasn't been defeated
        if self._current_scene.get_name() == "Boss" and (not self.boss_defeated()):
            self.change_music(self._boss_music)

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
            #self._colliding_actors[0].respawn()
            self._colliding_actors[0].set_position(copy.copy(PLAYER_SPAWN))
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
        del self._messages
        self._messages = []
        self.remove_buttons()

    def remove_buttons(self):
        """
            Removes the buttons from the Cast.
        """
        del self._buttons
        self._buttons = {}

    def reset(self):
        """
            Reset all Scene knowledge that the Scene Manager has
            Keeps Player and HUD data
        """
        # Reset the Scene and the win condition
        self._current_scene = None
        self._win = False
        
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