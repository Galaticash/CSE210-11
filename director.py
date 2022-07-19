from scene_manager import Scene_Manager
from actors.player import *
from actors.message import Message, Temp_Message
from actors.button import Button
from GraphicInterface import Window
from mouse_input import Mouse_Input
from Scene import *
from constants import *

class Director():
    """
        Directs the inner workings of the game.
    """
    def __init__(self):
        # Determine if the game is over.
        self._game_over = False
        self._win = False
        # Determine iwf the window should close (exit program).
        self._window_close = False
        # Add all the constants
        self._max_x = WINDOW_MAX_X
        self._max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE
        self._actor_size = ACTOR_WIDTH

        # Create a Window to display things on
        self._window = Window(self._max_x, self._max_y)

        self._game_scenes = {}

        # Create a Scene Manager to manage the current Scene and the collisions between Actors in that Scene
        self._scene_manager = Scene_Manager(self._max_x, self._max_y)

        # Create a Mouse_input
        self._mouse = Mouse_Input()

    def create_scenes(self):
        """
            Creates all the scenes in the game and adds their connections
        """
        # {"SPAWN": Scene() }
        self._game_scenes["TEST"] = TestScene()
        self._game_scenes["SPAWN"] = Spawn_scene()
        self._game_scenes["BOSS"] = Boss_Scene()
        self._game_scenes["ONE"] = Scene1()
        self._game_scenes["TWO"] = Scene2()
        self._game_scenes["HIDDEN"] = Hidden_Scene()

        # Add connections for the Spawn
        self._game_scenes["SPAWN"].add_connection("TOP", "BOSS")
        self._game_scenes["SPAWN"].add_connection("RIGHT", "ONE")
        self._game_scenes["SPAWN"].add_connection("LEFT", "HIDDEN")
        self._game_scenes["SPAWN"].add_connection("BOTTOM", "TWO")

        # Add connections for Boss
        self._game_scenes["BOSS"].add_connection("BOTTOM", "SPAWN")

        # Add connection for One
        self._game_scenes["ONE"].add_connection("LEFT", "SPAWN")

        # Add connection for Two
        self._game_scenes["TWO"].add_connection("TOP", "SPAWN")
        
        # Add connection for Hidden room
        self._game_scenes["HIDDEN"].add_connection("RIGHT", "SPAWN")

    def start_game(self):
        """
            Begin the Space game. Creates the Player and puts them into the starting scene.
        """
        # Load the images used in the game
        self._window.load_images("assets")

        # Creates the game's scenes
        self.create_scenes()

        # Add the Player (user) and Enemies to the Cast.

        self._scene_manager.add_player(Player(PLAYER_NAME, PLAYER_SPAWN, ACTOR_WIDTH, ACTOR_HEIGHT))
        
        # Start at the SPAWN scene
        self._scene_manager.setup_scene(self._game_scenes["SPAWN"])
        
    def update_game(self):
        """
            Updates all members of the cast while the game is not over (self._game_over)
        """
        # If the game is not over,
        if not self._game_over:
            # Continue playing the game,
            #   Checks if the game is over (the Player has died)
            self._game_over = not(self._scene_manager.continue_game())
            self._win = self._scene_manager.boss_defeated()
            # DEBUG: Immediate game over
            #self._game_over = True
            
            # If the game has just ended in the last check
            if self._game_over:
                self.add_game_over()
            else:
                # Check if the Player is trying to change Scenes
                next_scene = self._scene_manager.check_collisions()
                if not (next_scene == None):
                    if next_scene == "BOSS" and not (self._scene_manager.get_player().has_key()):
                        # Tell the Player to get the key
                        self._scene_manager.add_message(Temp_Message(Point(450, 300), FONT_SIZE, "Must first have the key", 4))
                    else:
                        # Move the Player to the next scene
                        self._scene_manager.setup_scene(self._game_scenes[next_scene])
        else:
            # Check for "Play Again" or "Exit" click            
            mouse_position = self._mouse.click_position()

            # If the mouse was clicked,
            if not (mouse_position == None):
                # Check if the user chose to play again (based on which button is clicked).
                # Returns three values None: no button clicked, True: Play Again clicked, False: Exit clicked
                play_again = self._scene_manager.check_replay_buttons(mouse_position)
                # If the user actually pressed a button,
                if not (play_again == None):
                    if play_again:
                        # Reset the game if "Play Again" was clicked.
                        self.replay()
                    else:
                        # Exit the game if "Exit" was clicked.
                        self._window_close = True
                        return

        # Updates the visuals of the game.
        self._window.update(self._scene_manager)

        # Checks if the window should close (X button pressed).
        self._window_close = self._window.should_close()

    def add_game_over(self):
        """
            Adds the "Game Over" Menu to the displayed cast.
        """
        # Math to figure out where "Game Over" and it's buttons should be placed
        game_over_pos = Point((self._max_x - (int(len("Game Over")/2 * GAME_OVER_SIZE)))//2, (self._max_y - GAME_OVER_SIZE)//2)
        x_offset = GAME_OVER_SIZE * 2
        y_offset = int(GAME_OVER_SIZE * 1.5)
        
        # Add the Game Over Message.
        if self._scene_manager.boss_defeated():
            self._scene_manager.add_message(Message(game_over_pos, GAME_OVER_SIZE, "You Win!"))
        else:
            self._scene_manager.add_message(Message(game_over_pos, GAME_OVER_SIZE, "Game Over"))
        
        # Add Play Again and Exit Buttons.
        self._scene_manager.add_button("PLAY_AGAIN", Button(Point(game_over_pos.get_x() - (x_offset//2), game_over_pos.get_y() + y_offset), BUTTON_SIZE, "Play Again"))
        self._scene_manager.add_button("EXIT", Button(Point(game_over_pos.get_x() + (2 * x_offset), game_over_pos.get_y()+ y_offset), BUTTON_SIZE, "Exit"))

    def replay(self):
        """
            Resets the game.
        """
        # Reset game over/win variables
        self._game_over = False
        self._win = False
        
        self.create_scenes() # Reset the Scenes (Enemies respawned, etc)

        # Restart the Scene Manager with the Spawn Scene
        self._scene_manager.restart_game(self._game_scenes["SPAWN"])
    
    def get_game_over(self):
        """
            Determines if the game is over (return to main menu).
        """
        return self._game_over

    def get_window_close(self):
        """
            Returns to main if the game window has been closed.
        """
        return self._window_close

    def end_game(self):
        """
            Ends the game by closing the window. Additional things can be added
              like adding a game over animation/screen.
        """
        self._window.unload_images()
        self._window.close()

# Game can also just be run from Director
if __name__ == "__main__":
    astronaut_game = Director()
    astronaut_game.start_game()
    # Slightly different here, window will not close until user presses the "X" button.
    while not astronaut_game.get_window_close():
        astronaut_game.update_game()
    astronaut_game.end_game()