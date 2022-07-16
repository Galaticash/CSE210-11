import os
import pyray
from pyray import Rectangle
import pathlib
from actors.image import Image

from constants import DIRECTIONS, UI_Y_POS, WINDOW_MAX_X, ROTATION

FRAME_RATES = {"easy": 12, "medium": 30, "hard": 60}
FRAME_RATE = FRAME_RATES["medium"]

"""
    Note: The GUI does NOT update the position of anything, only displays their current position.
    Requires:
        A Cast with:
            Player, inherits from Collision Actor
            Enemies, inherits from Collision Actor
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
        self._textures = {}

        # Creates a Window of size width x height, and the given title.
        pyray.init_window(self._width, self._height, "Space Game - Team F")
        
        # Has a const set Frame Rate, limits number of updates
        pyray.set_target_fps(FRAME_RATE)
        self._hitbox_test_color = (255, 0, 0, 50)
        self._hitbox_test_hit_color = (255, 0, 0, 200)

        self._background_color = (255, 162, 87, 255)
        self._GUI_space = 100

    def load_images(self, directory):
        """
            Loads all images in the assets folder to the textures dictionary
        """
        filepaths = self._get_filepaths(directory, [".png", ".gif", ".jpg", ".jpeg", ".bmp"])
        for filepath in filepaths:
            if filepath not in self._textures.keys():
                texture = pyray.load_texture(filepath)
                self._textures[filepath] = texture

    def unload_images(self):
        """
            Unloads the images from memory.
        """
        for texture in self._textures.values():
            pyray.unload_texture(texture)
        self._textures.clear()

    def _get_filepaths(self, directory, filter):
        """
            Gets all the filepaths for each image in the assets folder
            Edited to find items within sub folders
        """
        filepaths = []
        files = os.listdir(directory)
        for file in files:
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
            # If there is a sub_folder
            elif extension == "":
                # Rename, know it is NOT a singular file
                folder = file
                # Wont load files from file named NotLoaded
                if not(folder == "NotLoaded"):
                    sub_directory = directory + "\\" + folder
                    sub_files = os.listdir(sub_directory)
                    # Add all files within it to the files to look over
                    for sub_file in sub_files:            
                        files.append(folder + "\\" + sub_file)
        return filepaths

    # def _get_rectangle(self, actor):
    #     return Rectangle(actor.get_x(), actor.get_y(), actor.get_hitbox().right - actor.get_hitbox().left, actor.get_hitbox().bottom - actor.get_hitbox().top)

    def _print_circle(self, actor):
        """
            Print a green circle at the actor's point position.
        """
        pyray.draw_circle(actor.get_x(), actor.get_y(), 20, pyray.GREEN)

    def _flip_image(self, texture):
        pass

    def _print_actor_image(self, actor):
        """
            Prints the given actor's image on the screen.
        """
        # DEBUG: Prints Hitbox
        # self._print_hitbox(actor.get_hitbox())
        # DEBUG: Prints point position
        #pyray.draw_circle(actor.get_x(), actor.get_y(), 10, pyray.GREEN)
        
        redraw = actor.get_facing()[0] < 0

        # Checks if the actor has an image
        image = actor.get_display()
        if not (image == ""):
            # Gets the filepath for the image
            filepath = image.get_filepath()
            try:
                # texture = self._textures[filepath]
                texture = self._textures[filepath]
            except KeyError:
                print(f"Invalid filepath, {actor.get_name()}: {filepath}")
                return

            size = actor.get_size() * image.get_scale()
            scale = size // texture.width # Make sure it fits within the box

            # ROTATION
            rotation = image.get_rotation()

            # Actor Position is the center
            center_x = actor.get_x()
            center_y = actor.get_y()

            width_radius = texture.width//2 * scale
            height_radius = texture.height//2 * scale

            # Calculate top/left print position from center
            position_x = center_x - width_radius
            position_y = center_y - height_radius

            # If rotated, adjust position so the image
            #  stays centered on the Actor's Position
            if rotation == ROTATION[1]:
                position_x = center_x + height_radius
            elif rotation == ROTATION[2]: 
                position_x = center_x + width_radius
                position_y = center_y + height_radius
            elif rotation == ROTATION[3]: 
                position_y = center_y + width_radius
            
            # Convert position to a 2D Vector
            raylib_position = pyray.Vector2(position_x, position_y)
            
            # NOTE: MUST put full Alpha or the image is not shown
            tint = image.get_tint()

            # Flipping left
            if redraw:
                # print("Draw Left")
                #tint = pyray.BLACK
                
                # pyray.Texture
                pass

            pyray.draw_texture_ex(texture, raylib_position, rotation, scale, tint)
        else:
            print(f"There is no image for the actor at position [{actor.get_x()}, {actor.get_y}]")

    def _print_actor(self, actor):
        """
            Prints the given actor on the screen. All 
             variables are recieved from the actor itself.
        """
        pyray.draw_text(actor.get_display(), actor.get_x(), actor.get_y(), actor.get_size(), actor.get_color())

    def _print_counter(self, counter):
        """
            Draws a Counter with in a Image x count format
        """
        # some math to figure out how far away from the image it should be
        buffer_x = counter.get_size()
        buffer_y = counter.get_size()//2
        pyray.draw_text("x " + str(counter.get_count()), counter.get_x() + buffer_x, counter.get_y() - buffer_y, counter.get_size(), counter.get_color())
        self._print_actor_image(counter)

    def _print_button(self, button):
        """
            Prints the given button on the board. Has a box 
             surrounding it to differentiate itself as a button.
        """        
        # self._print_hitbox(button.get_hitbox(), button.get_color())
        pyray.draw_text(button.get_display(), button.get_x(), button.get_y(), button.get_size(), button.get_text_color())
        
    def _print_hitbox(self, hitbox, color = ""):
        """
            Draws a given hitbox. Must be printed before text, 
             otherwise the Rectangle will draw on top of the text.
        """
        hitbox_color = color
        if color == "":
            # Draw a rectangle
            hitbox_color = self._hitbox_test_hit_color if hitbox.get_is_hit() else self._hitbox_test_color

        pyray.draw_rectangle(hitbox.left, hitbox.top, hitbox.right - hitbox.left, hitbox.bottom - hitbox.top, hitbox_color)

        # Draw the outline
        # Draw the top line
        pyray.draw_line(hitbox.left, hitbox.top, hitbox.right, hitbox.top, color)
        # Bottom
        pyray.draw_line(hitbox.left, hitbox.bottom, hitbox.right, hitbox.bottom, color)
        # Left
        pyray.draw_line(hitbox.left, hitbox.top, hitbox.left, hitbox.bottom, color)
        # Right
        pyray.draw_line(hitbox.right, hitbox.top, hitbox.right, hitbox.bottom, color)

    def _print_rock(self, rock):
        """
            Draw a Pyray Rectangle instead of an image/png
        """
        # Put the Rock's position, size, etc
        pyray.draw_rectangle()

    def update(self, cast):
        """
            Draws a frame of the Game given the Cast of Actors.
        """
        # Refreshes the board to black
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        pyray.draw_rectangle(0, self._GUI_space, self._width, self._height, self._background_color)

        # TODO: Print background of the scene (gotten from Cast)

        # DEBUG: Printing the walls/exit points
        walls = cast.get_walls()
        for direction in DIRECTIONS:
            #self._print_circle(walls[direction])
            self._print_hitbox(walls[direction].get_hitbox(), pyray.BLUE)

        # Updates the Colliding Actors
        for actor in cast.get_colliders():
            self._print_actor_image(actor)

        # TODO: Draw any rocks, objects, etc (decoration?)
        for item in cast.get_bg_objects():
            self._print_actor_image(item)

        # Objects with colliders
        for item in cast.get_objects():
            self._print_actor_image(item)

        # Draw the GUI
        pyray.draw_rectangle(0, 0, WINDOW_MAX_X, UI_Y_POS, pyray.BLACK)

        # Prints the HUD items (Counter)
        for item in cast.get_HUD():
            self._print_counter(item)

        # Updates the Messages
        for message in cast.get_messages():
            self._print_actor(message)

        # Updates the Buttons
        for button in cast.get_buttons():
            #self._print_circle(button)
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