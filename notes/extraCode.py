# old code?
    # def _set_limits(self):
    #     # The position is at the Top Left (determined by python.draw_text/etc)
    #     self._limits[DIRECTIONS[0]] = (self._position.get_y() - self._size//2) - self._padding
    #     self._limits[DIRECTIONS[2]] = (self._position.get_x() - (self._size//2)) - self._padding

    #     # Top point + (down) font_size = Bottom point
    #     self._limits[DIRECTIONS[1]] = (self._position.get_y() + self._size//2) + self._padding

    #     # Left point + (right) font_size * width = Right point
    #     # The right side of the hitbox must be adjusted to the length of the symbol
    #     self._limits[DIRECTIONS[3]] = (self._position.get_x() + (self._size//2)) + self._padding

        # How many pixels the Actor travels per Move method call.

## GRAPHIC INTERFACE
# # When I was printing actors, wanted to test Enemy Paths
# # So I thought it would be cool to keep the code
# try:
#     # DEBUG: See enemy pathing -ish
#     route_points = actor._route
#     for point in route_points:
#         pyray.draw_circle(point.get_x(), point.get_y(), 5, pyray.GREEN)
#     goal_point = actor._goal_position
#     pyray.draw_circle(goal_point.get_x(), goal_point.get_y(), 5, pyray.YELLOW)
#     pyray.draw_line(actor.get_x(), actor.get_y(), goal_point.get_x(), goal_point.get_y(), pyray.RED)
# except:
#     # Whoopsie! The actor isn't an Enemy/doesn't have a _route
#     pass


## EXTRA SCENE ACTORS
        #self._objects.append(Pickup(BOSS_KEY_NAME + str(1), Point(450, 300), 1, PICKUP_SIZE))        
        #self._objects.append(Pickup(BULLET_NAME + str(2), Point(450, 400), 1, PICKUP_SIZE))
        #self._objects.append(Pickup(HEALTH_NAME + str(1), Point(450, 500), 1, PICKUP_SIZE))
        
        # There will be no enemies in the Spawn scene
        #self._enemies = []
        
        # Hitboxes that are not square will result in LOTS of errors, so only square things lol
        #self._objects.append(long_object("topWall1", Point(ACTOR_WIDTH * 2, ACTOR_WIDTH), WALL_SIZE, ROCK_BLACK_LONG, 0, 1.25))
        #self._objects.append(long_object("topWall1", Point(900 - ACTOR_WIDTH * 2, 100), WALL_SIZE, ROCK_BLACK_LONG, 1.25))
        
        #self._objects.append(collidable_obj("topWall2", Point(100, 300), ACTOR_WIDTH, ROCK_BLACK_LONG))
        #self._objects.append(collidable_obj("topWall3", Point(500, 500), ACTOR_WIDTH, ROCK_BLUE_LONG))
        
        #self._objects = [collidable_obj("Wall", Point(450, 100), ACTOR_WIDTH)]

        # Add some pickup items 
        #Pickup("Gem", Point(300, 150), 5, pickup_size)
        #Pickup("Life", Point(400, 150), 1, pickup_size)     
        #Pickup("Heart", Point(500, 150), 10, pickup_size)
        #Pickup("Bullet", Point(600, 150), 1, pickup_size)