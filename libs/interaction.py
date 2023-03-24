import math

from libs.vector import Vector
from libs.player import State


class Interaction:
    def __init__(self, player, keyboard, frame):
        self.player = player
        self.keyboard = keyboard
        self.frame = frame

    def update(self):
        for x in self.keyboard.keys:
            if x["down"]:
                if self.player.pos.x > self.frame.x + 25:
                    self.player.pos = Vector(0, self.player.pos.y)
                elif self.player.pos.x < -25:
                    self.player.pos = Vector(self.frame.x, self.player.pos.y)
                elif self.player.pos.y < -25:
                    self.player.pos = Vector(self.player.pos.x, self.frame.y)
                elif self.player.pos.y > self.frame.y + 25:
                    self.player.pos = Vector(self.player.pos.x, 0)

                if "vec" in x:
                    self.player.vel.add(x["vec"])
                elif "rot" in x:
                    if round(self.player.rot, 2) > 2 * math.pi:
                        self.player.rot -= 2 * math.pi
                    elif round(self.player.rot, 2) < -2 * math.pi:
                        self.player.rot += 2 * math.pi
                    self.player.rot += x["rot"]
                elif "action" in x:
                    if x["action"] == "shoot":
                        self.player.weapon.fire()
                        self.player.animation(State.MOVE)
                        x["down"] = False
                    elif x["action"] == "reload":
                        self.player.weapon.reload()
                        self.player.animation(State.RELOAD)
                        x["down"] = False
