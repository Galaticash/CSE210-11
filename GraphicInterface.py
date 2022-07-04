import pyray

FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["medium"]

"""
    Note: The GUI does NOT update the position of anything, only displays their current position.
    Requires:
        A Cast with:
            Player, inherits from Actor
            Messages, inherits from Actor
"""
class Window():
    """
        A Window which updates a visual representation of the state of the Game.
        __init__() will create the window
        .close() will close the window
        .update(self, cast) will update the graphical positions of all of the cast members
    """
    def __init__(self, width, height):
        # Given a width and height, creates a new window
        self._width = width
        self._height = height
        
        # Creates a Window of size width x height, and the given title.
        pyray.init_window(self._width, self._height, "Cycle Game - Team F")
        
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)

    def _print_actor(self, actor):
        """
            Prints the given actor on the board. All 
             variables are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_display(), actor.get_x(), actor.get_y(), actor.get_font_size(), actor.get_color())

    def _print_player(self, player):
        """
            Prints an image representation of the Player
            Testing with using sprites/images instead of just ASCII characters.
        """
        # TODO: Figure out what the 'model' class is, how to make a model?
        pyray.draw_model()
        pass

    def _print_button(self, button):
        """
            Prints the given button on the board. Has a box 
             surrounding it to differentiate itself as a button.
        """        
        self._print_hitbox(button.get_hitbox())
        pyray.draw_text(button.get_display(), button.get_x(), button.get_y(), button.get_font_size(), button.get_color())
        
    def _print_hitbox(self, hitbox):
        """
            Draws a given hitbox. Must be printed before text, 
             otherwise the Rectangle will draw on top of the text.
        """
        # Draw a rectangle
        pyray.draw_rectangle(hitbox.left, hitbox.top, hitbox.right - hitbox.left, hitbox.bottom - hitbox.top, pyray.WHITE)

        # Draw the outline
        # Draw the top line
        pyray.draw_line(hitbox.left, hitbox.top, hitbox.right, hitbox.top, pyray.RAYWHITE)
        # Bottom
        pyray.draw_line(hitbox.left, hitbox.bottom, hitbox.right, hitbox.bottom, pyray.RAYWHITE)
        # Left
        pyray.draw_line(hitbox.left, hitbox.top, hitbox.left, hitbox.bottom, pyray.RAYWHITE)
        # Right
        pyray.draw_line(hitbox.right, hitbox.top, hitbox.right, hitbox.bottom, pyray.RAYWHITE)

    def update(self, cast):
        """
            Draws a frame of the Game given the Cast of Actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        # Updates the Collision Actors
        # TODO: Change to cast.get_colliders()
        for player in cast.get_players():
            self._print_actor(player)
            # DEBUG: Prints Hitbox
            self._print_hitbox(player.get_hitbox())

        # Updates the Messages
        for message in cast.get_messages():
            self._print_actor(message)

        # Updates the Buttons
        for button in cast.get_buttons():
            self._print_button(button)

        pyray.end_drawing()

    def should_close(self):
        """
            Returns if the user has indicated to close the window.
        """
        return pyray.window_should_close()

    def close(self):
        """
            Closes the window. Called at the end of the program.
        """
        pyray.close_window()