"""The `game_objects.py` module includes in-game objects"""


class Ptero:
    def __init__(self):
        self.x = 150
        self.y = 60
        self.prev_x = self.x
        self.prev_y = self.y


class Cactus:
    def __init__(self):
        self.x = 150
        self.y = 12
        self.prev_x = self.x
        self.prev_y = self.y


class Dino:
    def __init__(self):
        self.x = 15
        self.y = 12
        self.prev_x = self.x
        self.prev_y = self.y