# Final Game Project

## Requirements
- The program may be any type of game or interactive simulation. (User input and display that changes based on interaction)
- The program should use classes and instances.
- The program should apply the four principles of programming with classes.
- The program should use the libraries chosen in the course. (Pyray, etc)
- The program should be delivered through a version control system. (Git/GitHub)
- The program should be able to be run from the command line. (Runs as a Python file, etc)

## Week 11 - Maintainability
Learn about Maintainability and start the Final Project

### Practice - Batter

### Mastery Question (Wednesday 6/29)
What is maintainability and why is it important?

### Meeting (Thursday 6/30) - Ashley, John

### Mastery Question (Friday 7/1)
How did you ensure maintainability in your program's design?

## Classes used previously
Class | Description | Update?
----- | ----------- | ------ |
Director | Directs the inner workings of the game | yes - 
GraphicInterface | The GUI of the program, displays everything to the user | yes - print enemies
Cast | Contains lists of all the different types of Actors to be updated and displayed (Collison Actors - Player and Enemies, Messages, Buttons, etc) | yes - adjust so there is a list of Collision Actors instead of Players
CollisionHandler | Handles all the collisions between Collision Actors for the Director | yes - allow collisions with ALL Collision Actors (find a flexible algorithm to check them all (works if num_enemies = 3 or num_enemies = 100))
Actor | The base class for items being displayed on the screen | no?
Message | A type of non-moving Actor that displays a message to the Window | no
Score | A specific type of Message that interacts with the Player class | maybe? Could change to HUD and display multiple things (lives, etc - any other attribute of the Player that needs to be visually displayed)
Button | A type of Message that has a Hitbox for the user to click, then a certain action is performed | maybe? Should actually implement color (GrahpicInterface display's button chosen color/colors?) Also is the Button in charge of the Action, or is it more a True/False update to the action back in Director (if button_clicked --> perform action)
Collision_Actor | A type of Actor that can interact with other Collision Actors when their Hitboxes collide | maybe? If displaying with sprites/images instead of ASCII characters
Hitbox | A bounded box that can detect if a Point is inside it (used for Button clicks and collision handling) | yes? update what happens when a collision happens, or would that be better handled in the Player/Collision Actor class or Collision Handler? 
Player | Can be moved around the screen by the user | yes?
player_input | The interface that decides the Player's movement from user input | maybe - additional buttons (attack, jump, etc) Also change walking/movement to pyray.up (w and up arrow both are 'up')
mouse_input | Checks where the mouse has been clicked (used for detecting Button clicks) | no?
color | The RGBA color value to be displayed | no
point | An [x,y] position of the Window | no

## New Classes
Class | Job
----- | ---
Enemy | Inherits from Collision Actor, 
Specific enemies | Different types of Enemies (different display, movement, hitpoints/damage, etc)
Pick up items | (Collision Actor - with movement removed (or could use it to animate floating?)
Scene | A Window Area where a Player can fight Enemies. The Scene can be cleared when all Enemies are defeated *subject to changes based on Game type.  Maybe this would be an adjusted version of Cast? Or each Scene has a Cast (enemies (created with Scene) + Player (receievd from the Director))? Scenes could also include the Main Menu

## Week 12 - Continuing Development
Continue Develpoing the Final Game

## Week 13 - Finishing the Final Project
Submit a recording of the game being played at the end of the week

### Final Project Due (Wednesday 7/13)
Might be able to continue working past then, but Wednesday is when the GitHub link is due.

### Mastery Question (Saturday 7/16)
*Can you fix bugs or add new features to your code without resorting to major refactoring? Why or why not?*

Add New Features by adding new things to the Director
- Add new Scenes
  - Add new Enemies to the Scenes
- Could change the number of lives, difficulty constants (damage, healthpoints) (read from a .txt file? or could make a constants.py)

### Project Demo (Saturday 7/16) *Voting Topic locked until 7/18
- A one minute recording showing off game and its mechanics

## Week 14 - Voting

### Final Video
Highlight the code you contributed to in the final project
- Introduce yourself
- Talk about what parts of the project you worked on
- Must be around 1 minute long
- Must have your face in the video
  - Recording with Zoom's share screen has worked well for me
