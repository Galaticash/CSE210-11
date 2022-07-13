from cast import Scene_Manager
from actors.player import *
from actors.message import Message
from actors.button import Button
from GraphicInterface import Window
from mouse_input import Mouse_Input
from Scene import Scene, Scene1, Boss_Scene
from actors.enemy import Enemy

DIRECTIONS = ["TOP", "BOTTOM", "LEFT", "RIGHT"]
WINDOW_MAX_X = 900
WINDOW_MAX_Y = 600
FONT_SIZE = 24
# Note: Actors are currenlty 24 pixels, 
# but they are dscaled up to be printed at this size
ACTOR_SIZE = 100

class Director():
    """
        Directs the inner workings of the game.
    """
    def __init__(self):
        # Determine if the game is over.
        self._game_over = False
        # Determine if the window should close (exit program).
        self._window_close = False
        # Add all the constants
        self._max_x = WINDOW_MAX_X
        self._max_y = WINDOW_MAX_Y
        self._font_size = FONT_SIZE
        self._actor_size = ACTOR_SIZE

        # Create a Window to display things on
        self._window = Window(self._max_x, self._max_y)

        self._game_scenes = {}

        # Create a Scene Manager to manage the current Scene and the collisions between Actors in that Scene
        self._cast = Scene_Manager(self._max_x, self._max_y)

        # Create a Mouse_input
        self._mouse = Mouse_Input()

    def create_scenes(self):
        """
            Creates all the scenes in the game
        """
        self._game_scenes["SPAWN"] = Scene()
        self._game_scenes["BOSS"] = Scene()
        self._game_scenes["TWO"] = Scene()
        

        self._game_scenes["SPAWN"]


        pass

    def start_game(self):
        """
            Begin the Space game. Creates the Player and puts them into the starting scene.
        """
        # Load the images used in the game
        self._window.load_images("assets")

        # Creates the game's scenes
        self.create_scenes()

        self._cast.setup_scene("SPAWN")

        # Add the Player (user) and Enemies to the Cast.
        self._cast.add_player(Player("Player", Point(int(self._max_x//2), self._actor_size + 10), self._actor_size))
        self._cast.add_collider(Enemy("Enemy1", Point(int(self._max_x * 2/3), self._max_y//2), self._actor_size))
        self._cast.add_collider(Enemy("Enemy2", Point(int(self._max_x * 1/3), self._max_y//2), self._actor_size))
        self._cast.add_collider(Enemy("Enemy3", Point(int(self._max_x * 2/3) + 75, self._max_y//2), self._actor_size))
        self._cast.add_collider(Enemy("Enemy4", Point(int(self._max_x * 1/3) - 75, self._max_y//2), self._actor_size))

        # Add all scene elements to the cast
        #   Add all enemies
        #   Add all walls/objects
        # TODO: Add Enemies class and subclasses (specific types of enemies, a boss as well?)

    def update_game(self):
        """
            Updates all members of the cast while the game is not over (self._game_over)
            TODO: Figure out specifics of the game/what ends the game, win condition?
            TODO: Adjust for Final Game
        """
        # Move all members of the cast.
        self._cast.move_colliders()
        self._cast.check_actions()
        self._cast.check_collisions()
        
        # Check if the game is currently over
        if not self._game_over:
            # TODO: Insert some kind of check for game over, Player lives = 0, etc
            if self._game_over:
                self.add_game_over()
        else:
            # Check for "Play Again" or "Exit" click            
            mouse_position = self._mouse.click_position()

            # If the mouse was clicked,
            if not (mouse_position == None):
                # Check if the user chose to play again (based on which button is clicked).
                play_again = self._cast.check_replay_buttons(mouse_position)
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
        self._window.update(self._cast)

        # Checks if the window should close (X button pressed).
        self._window_close = self._window.should_close()

    def add_game_over(self):
        """
            Adds the "Game Over" Menu to the displayed cast.
            TODO: Adjust for Final Game
        """
        # Lots of math to determine the location, would be better if it was more concise.
        game_over_size = self._font_size * 2
        button_size = int(self._font_size * 1.5)
        center = [(self._max_x - (int(len("Game Over")/2 * game_over_size)))//2, (self._max_y - game_over_size)//2]
        x_offset = game_over_size * 2
        y_offset = int(game_over_size * 1.5)
        
        # Add the Game Over Message.
        self._cast.add_message(Message(self._max_x, self._max_y, center, game_over_size, "Game Over"))
        
        # Add Play Again and Exit Buttons.
        self._cast.add_button("PLAY_AGAIN", Button(self._max_x, self._max_y, [center[0] - (x_offset//2), center[1] + y_offset], button_size, "Play Again"))
        self._cast.add_button("EXIT", Button(self._max_x, self._max_y, [center[0] + (2 * x_offset), center[1] + y_offset], button_size, "Exit"))

    def replay(self):
        """
            Resets the game, but keeps the current scores.
            TODO: Adjust for Final Game
        """
        self._game_over = False

        # Removes game_over cast members (Game Over menu).
        self._cast.remove_game_over()
        self._cast.remove_buttons()

        # Resets the Player's Point position, Color?*
        self._cast.reset_player()
    
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
    cycle_game = Director()
    cycle_game.start_game()
    # Slightly different here, window will not close until user presses the "X" button.
    while not cycle_game.get_window_close():
        cycle_game.update_game()
    cycle_game.end_game()