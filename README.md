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
Director | () | yes - 
GraphicInterface | () | yes - print enemies
Cast | () | yes - adjust so there is a list of Collision Actors
CollisionHandler | () | yes - allow collisions with ALL Collision Actors
Actor | () | no?
Message | () | no
Score | () | maybe? Could change to HUD and display multiple things (lives, etc - any other attribute of the Player that needs to be visually displayed)
Button | () | maybe? Should actually implement color (GrahpicInterface display's button chosen color/colors?)
Collision_Actor | () | maybe? If displaying with sprites/images instead of ASCII characters
Hitbox | () | yes? update what happens when a collision happens, or would that be better handled in the Player/Collision Actor class or Collision Handler? 
Player | () | yes?
player_input | () | maybe - additional buttons (attack, jump, etc)
mouse_input | () | no?
color | () | no
point | () | no

## New Classes
- Enemy (Collision Actor)
- Types of enemies (Enemy)
- Pick up items (Collision Actor - with movement removed (or could use it to animate floating?)

## Week 12
Continue Develpoing the Final Game

## Week 13 (check back, Canvas unlocks 7/2)
Final Project Submisison
