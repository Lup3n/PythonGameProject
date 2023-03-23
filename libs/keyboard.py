import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector
import math

ROT: float = (2 * math.pi) / 100
SPEED: float = 0.5


class Keyboard:
    """
    Class that keeps track of the pressed buttons.
    Current checked buttons and their action:
        * W button     -> move up
        * A button     -> move left
        * S button     -> move down
        * D button     -> move right
        * R button     -> reload
        * Spacebar     -> shoot
        * Right arrow  -> turn right
        * Left arrow   -> turn left
    """

    def __init__(self):
        self.RIGHT = {
            "key": simplegui.KEY_MAP['right'],
            "rot": ROT,
            "down": False
        }
        self.LEFT = {
            "key": simplegui.KEY_MAP['left'],
            "rot": -ROT,
            "down": False
        }
        self.LOWER_W = {
            "key": simplegui.KEY_MAP['w'],
            "vec": Vector(0, -SPEED),
            "down": False
        }
        self.LOWER_S = {
            "key": simplegui.KEY_MAP['s'],
            "vec": Vector(0, SPEED),
            "down": False
        }
        self.LOWER_D = {
            "key": simplegui.KEY_MAP['d'],
            "vec": Vector(SPEED, 0),
            "down": False
        }
        self.LOWER_A = {
            "key": simplegui.KEY_MAP['a'],
            "vec": Vector(-SPEED, 0),
            "down": False
        }
        self.SPACE = {
            "key": simplegui.KEY_MAP['space'],
            "action": "shoot",
            "down": False
        }
        self.LOWER_R = {
            "key": simplegui.KEY_MAP['r'],
            "action": "reload",
            "down": False
        }

        self.keys = [self.RIGHT, self.LEFT, self.LOWER_W, self.LOWER_A, self.LOWER_S, self.LOWER_D, self.SPACE, self.LOWER_R]

    def keyDown(self, key):
        """
        Check if any of the buttons is being pressed, and if so, sets its boolean to ``True``
        :param key: The targeted key
        """
        for x in self.keys:
            if key == x["key"]:
                x["down"] = True

    def keyUp(self, key):
        """
        Check if any of the buttons is being released, and if so, sets its boolean to ``False``
        :param key: The targeted key
        """
        for x in self.keys:
            if key == x["key"]:
                x["down"] = False
