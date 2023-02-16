import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from libs.vector import Vector
import math
ROT = (2*math.pi)/100
SPEED = 0.5

class Keyboard:
    def __init__(self):
        self.right = {
            "key": simplegui.KEY_MAP['right'],
            "rot": ROT,
            "down": False
        }
        self.left = {
            "key": simplegui.KEY_MAP['left'],
            "rot": -ROT,
            "down": False
        }
        self.w = {
            "key": simplegui.KEY_MAP['w'],
            "vec": Vector(0, -SPEED),
            "down": False
        }
        self.s = {
            "key": simplegui.KEY_MAP['s'],
            "vec": Vector(0, SPEED),
            "down": False
        }
        self.d = {
            "key": simplegui.KEY_MAP['d'],
            "vec": Vector(SPEED, 0),
            "down": False
        }
        self.a = {
            "key": simplegui.KEY_MAP['a'],
            "vec": Vector(-SPEED, 0),
            "down": False
        }
        self.space = {
            "key": simplegui.KEY_MAP['space'],
            "action": "shoot",
            "down": False
        }
        self.r = {
            "key": simplegui.KEY_MAP['r'],
            "action": "reload",
            "down": False
        }

        self.keys = [self.right, self.left, self.w, self.a, self.s, self.d, self.space, self.r]

    def keyDown(self, key):
        for x in self.keys:
            if key == x["key"]:
                x["down"] = True


    def keyUp(self, key):
        for x in self.keys:
            if key == x["key"]:
                x["down"] = False
