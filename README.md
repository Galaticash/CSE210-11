# CSE 210 Final Project - Astronaut Adventures
This is a python project that was worked on by Ashley DeMott, John Lydiksen, and Hailey Phipps in CSE 210 - Programming with Classes. Over the course of 4 weeks, we created this Zelda-like game, and shared a video demo with our classmates. When we shared the demo, the game was capable of moving the Player between scenes and fighting enemies, but collisions were still a little buggy, and the game lacked sound (A feature every other demoed game had. L).

## Game Features
TODO
Lots of inheritance:
Actor - Collision Actor - Player, Scene - Boss Scene, Actor - Collision Actor - Pickup Item, etc

## Bugs
- Collisions still don't work really well, as the two colliders continually collide, bouncing back and forth. Could be solved with an invulnerability period, where the colliders cannot collide again (or, with only the initial collider - what happens when they are bounced through a wall?) for a set amount of time.
- Scenes are hardcoded~ish. New scenes can be added by editing the code (copy-paste a new Scene object, inheriting from Scene and renaming it and then adding it to the connections) But what if we wanted to change the scenes without editing code, like reading from a .txt document or some other kind of file that can store the Scene and its connections? A JSON may work well, have sections for each list of objects, and their positions, etc


## TODO
- Working on adding music/sound to the game. That was one feature that made the other games better than ours, but I wasn't able to set aside time to learn about pyray's audio system before demoing the project.
