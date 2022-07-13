from actors.Fighting_Actor import Fighting_Actor


SPIRTE_PATH = "assets\\Alien\\Alien_idle3.png"
ROUTE_BOUNDS = {"MIN": 100, "MAX": 500}


# TODO: Double check that Collision Actor has all shared code between Enemy and Player
class Enemy(Fighting_Actor):
    def __init__(self, position, size, image="", color="WHITE"):
        super().__init__(position, size, image, color)
        self._frames = ["Alien\\Alien_idle3.png"]
        self._velocity = [-1, 0]
    
    def move(self):
        """
            TODO: Implement some kind of algorithm for enemy movement
            Example: Move randomly within a certain range in the Scene
        """
        super().move()
        if self._position.get_x() < ROUTE_BOUNDS["MIN"]:
            self._velocity = [1, 0]
        elif self._position.get_x() > ROUTE_BOUNDS["MAX"]:
            self._velocity = [-1, 0]
