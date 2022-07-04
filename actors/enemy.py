from actors.collision_actor import Collision_Actor

# TODO: Double check that Collision Actor has all shared code between Enemy and Player
class Enemy(Collision_Actor):
    def __init__(self, max_x, max_y, font_size, color="WHITE"):
        super().__init__(max_x, max_y, font_size, color)

    def move():
        """
            TODO: Implement some kind of algorithm for enemy movement
            Example: Move randomly within a certain range in the Scene
        """
        super().move()
